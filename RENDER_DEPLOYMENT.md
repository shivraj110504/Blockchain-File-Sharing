# StoriumX - Render Deployment Guide

## Quick Deployment Steps

### 1. Prerequisites
- GitHub repository with your code
- MongoDB Atlas account with connection string
- Render account (free tier works)

### 2. Environment Variables

Set these environment variables in Render:

```
MONGODB_URI=mongodb+srv://shivarajtaware7192:QOyqCox4eXQAKud5@cluster0.al2kvje.mongodb.net/?appName=Cluster0
SECRET_KEY=your_random_secret_key_here_change_this
PORT=10000
BLOCKCHAIN_NODE_ADDR=https://your-app-name.onrender.com
FLASK_ENV=production
```

**Important:** Generate a strong SECRET_KEY for production:
```python
import secrets
print(secrets.token_hex(32))
```

### 3. Render Configuration

The project includes `render.yaml` for automatic deployment. Make sure it contains:

```yaml
services:
  - type: web
    name: storiumx
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn run_app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### 4. Deploy to Render

**Option A: Connect GitHub Repository**
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will auto-detect the `render.yaml` file
5. Add environment variables from step 2
6. Click "Create Web Service"

**Option B: Manual Deploy**
1. Push your code to GitHub
2. In Render, create a new Web Service
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn run_app:app`
5. Add environment variables
6. Deploy

### 5. Post-Deployment

1. **Test Authentication:**
   - Visit your Render URL
   - Create a new account with email/password
   - Verify login works

2. **Test File Upload:**
   - Upload a test file
   - Verify it appears in "My Files"
   - Download the file to confirm

3. **Test File Sharing:**
   - Create a second account
   - Share a file using the recipient's key
   - Login as recipient and view shared files

### 6. MongoDB Atlas Configuration

Your MongoDB connection string is already configured. Ensure:
- Network Access allows connections from anywhere (0.0.0.0/0) or add Render's IPs
- Database user has read/write permissions
- Database name will be automatically used from connection string

### 7. Troubleshooting

**Issue: App crashes on startup**
- Check Render logs for errors
- Verify all environment variables are set
- Ensure MongoDB connection string is correct

**Issue: Files not persisting**
- Files are stored in MongoDB (base64 encoded)
- Render's filesystem is ephemeral, but we handle this

**Issue: Login not working**
- Check SECRET_KEY is set
- Verify bcrypt is installed (should be in requirements.txt)
- Check browser console for errors

### 8. Custom Domain (Optional)

1. In Render dashboard, go to your service
2. Click "Settings" → "Custom Domain"
3. Add your domain and configure DNS

## Architecture Notes

- **Authentication:** Email/password with bcrypt hashing
- **File Storage:** MongoDB (base64 encoded for persistence)
- **Sessions:** Flask sessions with secure secret key
- **Blockchain:** Integrated peer functionality for file tracking

## Security Checklist

- ✅ Passwords are hashed with bcrypt
- ✅ Email validation implemented
- ✅ Session secret key from environment
- ✅ HTTPS enforced by Render
- ⚠️ Consider adding rate limiting for production
- ⚠️ Consider adding CSRF protection

## Support

For issues, check:
1. Render deployment logs
2. MongoDB Atlas logs
3. Browser console for frontend errors
