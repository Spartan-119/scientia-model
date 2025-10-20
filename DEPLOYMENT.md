# 🚀 Quick Deployment Guide

## Deploy to Streamlit Community Cloud (Free & Recommended)

This is the easiest way to share your financial projections with investors!

### Step 1: Prepare Your Repository

1. **Initialize Git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Scientia financial projections app"
   ```

2. **Push to GitHub**:
   - Create a new repository on GitHub (public or private)
   - Follow GitHub's instructions to push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/scientia-model.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)

2. Click **"New app"**

3. Fill in the details:
   - **Repository**: Select your GitHub repo `YOUR_USERNAME/scientia-model`
   - **Branch**: `main`
   - **Main file path**: `app.py`

4. Click **"Deploy"**

5. Wait 2-3 minutes for deployment

6. **Done!** Your app will be live at:
   ```
   https://YOUR_USERNAME-scientia-model-app-XXXXX.streamlit.app
   ```

### Step 3: Share with Investors

Simply share the URL! The app will:
- ✅ Load instantly in any browser
- ✅ Work on mobile devices
- ✅ Allow real-time adjustments
- ✅ Look professional and polished

### Making Updates

After deployment, any changes you push to GitHub will automatically update your app:

```bash
git add .
git commit -m "Updated assumptions"
git push
```

The app will redeploy automatically in 1-2 minutes.

---

## Alternative: Run Locally for Investor Meetings

If you're presenting in person, run locally:

```bash
streamlit run app.py
```

Then present from `http://localhost:8501`

**Tip**: Use the sidebar to adjust assumptions in real-time during Q&A!

---

## Troubleshooting

### App won't start?
- Check that all files are committed to Git
- Verify `requirements.txt` is in the root directory
- Check Streamlit Cloud logs for errors

### Need to keep it private?
- Use a private GitHub repository
- Streamlit Community Cloud supports private repos
- Only people with the URL can access your app

### Want a custom domain?
- Upgrade to Streamlit Teams (paid)
- Or use a reverse proxy with your own domain

---

## Security Notes for Investor Presentations

- ✅ No sensitive data is stored on servers
- ✅ All calculations happen in real-time
- ✅ No database or backend required
- ✅ Safe to share link with investors
- ⚠️ Don't commit actual financial data or secrets

---

**Need help?** Check [Streamlit Documentation](https://docs.streamlit.io) or the Streamlit Community Forum.

