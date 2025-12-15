# 🤖 Eco Avatar - AI Conversational Assistant

Real-time AI conversational avatar powered by OpenAI GPT-4.

## 🚀 Deploy to Vercel in 2 Minutes

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Sm0k367/eco-avatar)

### Quick Deploy Steps:

1. **Click "Deploy" button** above or go to: https://vercel.com/new
2. **Import repository:** `Sm0k367/eco-avatar`
3. **Add environment variable:**
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
   - Get it from: https://platform.openai.com/api-keys
4. **Click "Deploy"**
5. **Done!** Your app is live in ~2 minutes 🎉

## ✨ Features

- ✅ **AI Chat** - Powered by GPT-4
- ✅ **Voice Recording** - Speech-to-text with Whisper
- ✅ **Modern UI** - Beautiful dark theme interface
- ✅ **Mobile Responsive** - Works on all devices
- ✅ **Real-time** - Instant AI responses
- ✅ **Customizable** - Settings for voice, speed, volume

## 📁 Project Structure

```
eco-avatar/
├── api/                    # Vercel Serverless Functions
│   ├── chat.py            # AI chat endpoint
│   ├── transcribe.py      # Audio transcription
│   └── health.py          # Health check
├── public/                 # Static frontend
│   ├── index.html         # Main page
│   ├── styles.css         # Styling
│   └── app.js             # Frontend logic
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel configuration
└── README.md              # This file
```

## 🔑 Environment Variables

**Required:**
- `OPENAI_API_KEY` - Your OpenAI API key

**How to add in Vercel:**
1. Go to Project Settings → Environment Variables
2. Add `OPENAI_API_KEY` with your key
3. Select all environments (Production, Preview, Development)
4. Redeploy

## 🧪 API Endpoints

- `GET /api/health` - Health check
- `POST /api/chat` - Send message to AI
- `POST /api/transcribe` - Transcribe audio

### Test Health Endpoint:
```bash
curl https://your-app.vercel.app/api/health
```

### Test Chat:
```bash
curl -X POST https://your-app.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!", "session_id": "test"}'
```

## 💰 Cost

- **Vercel:** Free tier (100 GB bandwidth/month)
- **OpenAI API:** Pay-as-you-go (~$5-20/month depending on usage)

## 🛠️ Local Development

```bash
# Install Vercel CLI
npm install -g vercel

# Clone repository
git clone https://github.com/Sm0k367/eco-avatar.git
cd eco-avatar

# Run locally
vercel dev
```

## 📝 License

MIT License - feel free to use and modify!

## 📞 Support

- **Issues:** https://github.com/Sm0k367/eco-avatar/issues
- **Vercel Docs:** https://vercel.com/docs
- **OpenAI Docs:** https://platform.openai.com/docs

---

**Built with 💜 by Epic Tech AI**

**Ready to deploy?** Click the button above or visit: https://vercel.com/new
