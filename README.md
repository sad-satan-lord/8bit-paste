# 📄 README.md

```markdown
# NeoStream Paste (Serverless Pastebin)

A fully serverless paste-sharing application where your content lives entirely inside the URL.

## 🚀 Overview

NeoStream Paste is a privacy-first, zero-backend pastebin alternative. Instead of storing data on a server, it compresses your content and embeds it directly into the URL.

When someone opens the link, their browser decodes and renders the content instantly.

## ✨ Features

- 🔐 **Serverless & Private** – No backend, no database, no tracking
- ⚡ **Instant Sharing** – Generate a shareable link instantly
- 📦 **Compressed URLs** – Uses LZ-String for efficient encoding
- 🌐 **Client-Side Only** – Everything runs in the browser
- 🧩 **No Data Persistence** – Nothing is stored anywhere

## 🛠️ How It Works

1. User enters a title and content
2. Content is compressed using `LZ-String`
3. Compressed data is appended to the URL after `#`
4. Link is shared
5. On opening:
   - Browser reads the URL hash
   - Decompresses the data
   - Displays the paste

## 📌 Example Flow

```

Input → Compress → Encode → URL → Share → Decode → Display

````

## ⚙️ Tech Stack

- HTML / CSS / JavaScript
- [lz-string](https://github.com/pieroxy/lz-string)

## 🚫 Limitations

- URL length limits (browser-dependent)
- Not suitable for very large pastes
- No edit history or persistence

## 📦 Installation

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
````

Then simply open `index.html` in your browser.

## 🌍 Deployment

You can deploy this easily on:

* GitHub Pages
* Netlify
* Vercel

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

## 📜 License

MIT License

---

## 💡 Inspiration

A minimal, privacy-first alternative to traditional paste services.

```

---

# 🏷️ GitHub Repository Description (Short)

> A serverless pastebin that compresses content into the URL using LZ-String — no backend, no storage, fully client-side.

---

If you want, I can also:
- Make it more **aesthetic/dev-portfolio style**
- Add **badges (build, license, deploy)**
- Or tailor it to impress recruiters (especially for frontend roles)**
```
