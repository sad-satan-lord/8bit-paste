# 8-BIT PASTE

A beautiful, fully functional 8-bit themed pastebin application.

## Features

- **Retro 8-Bit Design:** Blocky fonts, pixelated borders, and native AMOLED dark mode with a Wheat Light mode toggle.
- **Serverless by Default:** Standard text and code pastes are compressed using LZ-String and stored directly in the shareable URL hash. No database required!
- **Server Backed for Media:** If you upload a file with `.m3u8` or `.mpd` extension, the frontend intelligently sends it to the backend server to be saved in a MongoDB database.
- **User Authentication:** Requires users to register and login (using JWTs) before they can save media playlists to the server.
- **VLC Protection:** Server-backed raw `.m3u8` and `.mpd` files cannot be viewed in standard web browsers. The backend verifies the `User-Agent` and only permits media players like VLC to read the files.
- **Local History:** Your last 10 pastes are saved in your browser's `localStorage` and displayed on the home page.
- **Edit Mode:** Easily edit an existing paste by loading it back into the editor with the click of a button.

## Architecture Guide & Explanation

This application utilizes a unique **hybrid architecture** to balance performance, cost (zero database overhead for text), and security constraints for specific file types.

### 1. Serverless Mode (For Text/Code)
When you create a standard paste (like `script.js` or `notes.txt`), the application operates **100% serverlessly**. 
- The JavaScript reads your title and content.
- It compresses this data heavily using the `LZ-String` algorithm.
- It encodes this compressed data into a safe string and appends it to your URL after the `#view/` hash (e.g., `http://localhost:5000/#view/COMPRESSED_DATA`).
- When someone visits that link, their browser reads the hash, decompresses the data, and displays the paste. **Your text is never saved on any server.**

### 2. Server-Backed Mode & Authentication (For Media Playlists)
Media playlists like `.m3u8` and `.mpd` files present a unique challenge: they must be read natively by media players (like VLC), which do not execute JavaScript and therefore cannot decompress a serverless URL hash.
- When you save a file ending in `.m3u8` or `.mpd`, the frontend detects the extension.
- It checks if you are logged in. If not, it redirects you to the login page.
- It sends an HTTP POST request to the Python Flask backend with your JWT in the `Authorization` header.
- The backend verifies the token, generates a UUID, and stores the paste content along with your username in the **MongoDB** database.
- The URL generated is a clean, server-backed link (e.g., `http://localhost:5000/#server/UUID`).

### 3. VLC / Media Player Protection
A core requirement of this application is that raw media playlists should *only* open in media players, not standard web browsers.
- When you click "Raw" on a server-backed paste, it routes to `http://localhost:5000/raw/UUID`.
- The Flask backend queries MongoDB for the file.
- Before serving the file, Flask inspects the HTTP `User-Agent` header sent by the client.
- If the `User-Agent` contains signatures of common web browsers (`mozilla`, `chrome`, `safari`, etc.) but *does not* contain `vlc`, the server responds with a `403 Access Denied` error.
- If VLC requests the file, it serves the raw playlist text with a `text/plain` mimetype, allowing the video to play securely.

## Setup & Running

This project uses a lightweight Python Flask backend to handle the MongoDB media storage, JWT authentication, and user-agent routing.

1. **Install Dependencies:**
   Make sure you have Python installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables:**
   The application requires a MongoDB database and a secret key for JWTs.
   ```bash
   export MONGO_URI="mongodb+srv://<username>:<password>@cluster.mongodb.net/"
   export SECRET_KEY="your-super-secret-key"
   ```
   *(If not provided, it will default to a local database and a default development secret key).*

3. **Run the Server:**
   ```bash
   python server.py
   ```
   The application will be available at `http://127.0.0.1:5000/`.

## Files
- **`index.html`:** The single-page frontend application. Handles UI, URL routing, compression, and API calls.
- **`server.py`:** The Flask backend that serves the HTML and acts as an API and file server for `.m3u8`/`.mpd` pastes.
- **`requirements.txt`:** Python dependencies.
