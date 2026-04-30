from pymongo import MongoClient
import uuid
from flask import Flask, request, jsonify, send_file, Response, send_from_directory
import os
import jwt
import datetime
import bcrypt
from functools import wraps

app = Flask(__name__)
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['8bit_paste']
pastes_collection = db['pastes']
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', '8bit-super-secret-key-change-in-prod')
users_collection = db['users']

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(" ")[1]
        
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
            
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = users_collection.find_one({'username': data['username']})
            if not current_user:
                raise Exception("User not found")
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
            
        return f(current_user, *args, **kwargs)
    return decorated

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400
        
    username = data['username']
    password = data['password']
    
    if users_collection.find_one({'username': username}):
        return jsonify({'message': 'User already exists!'}), 409
        
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    users_collection.insert_one({
        'username': username,
        'password': hashed_password.decode('utf-8')
    })
    
    return jsonify({'message': 'Registered successfully!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
        
    user = users_collection.find_one({'username': data['username']})
    
    if not user:
        return jsonify({'message': 'User not found'}), 401
        
    if bcrypt.checkpw(data['password'].encode('utf-8'), user['password'].encode('utf-8')):
        token = jwt.encode({
            'username': user['username'],
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=7)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({'token': token, 'username': user['username']})
        
    return jsonify({'message': 'Wrong password'}), 401


@app.route('/')
def index():
    return send_file('index.html')

@app.route('/api/save', methods=['POST'])
@token_required
def save_paste(current_user):
    data = request.json
    if not data or 'content' not in data:
        return jsonify({'error': 'No content provided'}), 400
    
    title = data.get('title', 'untitled.txt')
    content = data['content']
    paste_id = str(uuid.uuid4())
    
    pastes_collection.insert_one({
        'id': paste_id,
        'title': title,
        'content': content,
        'author': current_user['username']
    })
    
    return jsonify({'id': paste_id, 'url': f'#server/{paste_id}'}), 200

@app.route('/api/paste/<paste_id>', methods=['GET'])
def get_paste(paste_id):
    paste = pastes_collection.find_one({'id': paste_id})
    
    if paste:
        return jsonify({'title': paste['title'], 'content': paste['content']}), 200
    return jsonify({'error': 'Paste not found'}), 404

@app.route('/raw/<paste_id>', methods=['GET'])
def get_raw(paste_id):
    paste = pastes_collection.find_one({'id': paste_id})
    
    if not paste:
        return "Paste not found", 404
        
    title = paste['title']
    content = paste['content']
    
    # Check if it's m3u8 or mpd
    is_media = title.endswith('.m3u8') or title.endswith('.mpd')
    
    if is_media:
        # Layer of protection: Block common browsers
        user_agent = request.headers.get('User-Agent', '').lower()
        blocked_agents = ['mozilla', 'chrome', 'safari', 'webkit', 'opera', 'edge']
        
        # If any blocked word is in the user agent, but it's not vlc, block it.
        # Most standard browsers have 'mozilla' or 'chrome' or 'safari' in them.
        is_browser = any(agent in user_agent for agent in blocked_agents)
        is_vlc = 'vlc' in user_agent
        
        # If it's a browser and not vlc, block it.
        if is_browser and not is_vlc:
             return "Access denied: This file can only be opened in a media player like VLC.", 403

    return Response(content, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
