# Working Demo - https://8bit-paste.netlify.app/
# 🎮 8BIT-PASTE

> **PASTE. SHARE. ENCODE. THAT’S IT.**

🟣 A retro-styled, serverless pastebin where your data lives *entirely inside the URL*.

No server.
No database.
No tracking.
**Just a link.**
TODOS :
PASTEL THEME
LocalDB
More compressed URL 

---

## 🕹️ FEATURES

✨ **Serverless**

* Zero backend. Zero infrastructure.

🔐 **Private by Design**

* Your data is never stored anywhere.

⚡ **Instant Sharing**

* Generate a shareable link in milliseconds.

💾 **Compressed URLs**

* Powered by `LZ-String` for efficient encoding.

👾 **8-Bit UI**

* Pixel-perfect retro aesthetic.

---

## ⚙️ HOW IT WORKS

```
[ Your Text ]
      ↓
 Compress (LZ-String)
      ↓
 Encode
      ↓
 Embed in URL (#)
      ↓
 Share Link
      ↓
 Decode + Decompress
      ↓
 Display in Browser
```

📌 The entire paste is stored in the URL hash (`#`), meaning:

* It never touches a server
* It exists only in the link you share

---

## 🧪 DEMO FLOW

1. Type your title and content
2. Click generate/share
3. Copy the link
4. Open it anywhere
5. Boom — your paste appears instantly

---

## 🛠️ TECH STACK

* HTML
* CSS
* JavaScript
* [`lz-string`](https://github.com/pieroxy/lz-string)

---

## ⚠️ LIMITATIONS

* URL length is limited by browsers
* Not ideal for very large pastes
* No edit history or persistence

---

## 🚀 GETTING STARTED

```bash
git clone https://github.com/your-username/8bit-paste.git
cd 8bit-paste
```

Open `index.html` in your browser.

That’s it. No build. No setup. No nonsense.

---

## 🌍 DEPLOYMENT

Works anywhere static sites are supported:

* GitHub Pages
* Netlify
* Vercel
* Any static host

---

## 🤝 CONTRIBUTING

Pull requests are welcome.
If you’ve got a cool idea, open an issue first.

---

## 📜 LICENSE

MIT License

---

## 💜 MADE WITH 8-BIT LOVE

```
██████╗  █████╗ ███████╗████████╗███████╗
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██████╔╝███████║███████╗   ██║   █████╗  
██╔═══╝ ██╔══██║╚════██║   ██║   ██╔══╝  
██║     ██║  ██║███████║   ██║   ███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
```
