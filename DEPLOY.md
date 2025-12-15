# 🚀 Deploy Eco Avatar to Vercel

## ✅ Quick Deploy (2 Minutes)

### Step 1: Go to Vercel
Open: **https://vercel.com/new**

### Step 2: Import Repository
1. Click **"Import Git Repository"**
2. Select: **`Sm0k367/eco-avatar`**
3. Click **"Import"**

### Step 3: Configure (Use Defaults)
- **Framework Preset:** Other
- **Root Directory:** `./`
- **Build Command:** (leave empty)
- **Output Directory:** `public`

### Step 4: Add Environment Variable
**CRITICAL:** Add your OpenAI API key:
- **Name:** `OPENAI_API_KEY`
- **Value:** `sk-your-openai-key-here`
- **Environments:** Select all (Production, Preview, Development)

### Step 5: Deploy
Click **"Deploy"** button

### ✅ Done!
Your app will be live at: `https://eco-avatar-[random].vercel.app`

---

## 🔑 Get OpenAI API Key

1. Go to: https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (starts with `sk-`)
4. Use it in Step 4 above

---

## 🧪 Test Your Deployment

### 1. Health Check
Visit: `https://your-app.vercel.app/api/health`

Should return:
```json
{
  "status": "healthy",
  "platform": "vercel",
  "openai_configured": true
}
```

### 2. Test Chat
1. Open: `https://your-app.vercel.app`
2. Type: "Hello!"
3. Verify AI responds

---

## ⚠️ Troubleshooting

### Issue: "API Error" on homepage
**Solution:** Add OPENAI_API_KEY environment variable and redeploy

### Issue: Health check shows `"openai_configured": false`
**Solution:** 
1. Go to Project Settings → Environment Variables
2. Add OPENAI_API_KEY
3. Click "Redeploy"

### Issue: 404 on /api/health
**Solution:** Vercel is still deploying. Wait 1-2 minutes and refresh.

---

## 📊 What's Included

✅ **Serverless Python Functions** - All API endpoints work  
✅ **Modern Frontend** - Beautiful UI with dark theme  
✅ **Voice Recording** - Speech-to-text capability  
✅ **Health Check** - Monitor API status  
✅ **Error Handling** - Clear error messages  

---

## 💰 Cost

- **Vercel:** Free (100 GB/month)
- **OpenAI:** ~$5-20/month (usage-based)

---

## 🎉 Success!

Once deployed, share your app with the world!

**Your app:** `https://your-project.vercel.app`

---

**Need help?** Check the main README.md or open an issue on GitHub.
