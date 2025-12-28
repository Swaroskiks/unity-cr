# Deployment Guide

Follow these steps to deploy the Unity Project Presentation site on your VPS.

## Prerequisites
- A VPS (Ubuntu/Debian recommended)
- Python 3.12+ installed
- Node.js 20+ installed

## 1. Transfer Files
Copy the entire project folder to your VPS. You can use `scp` or `rsync`.
```bash
# From your local machine
scp -r /path/to/quiz-app user@your-vps-ip:~/unity-presentation
```

## 2. Backend Setup (`unity-api`)
SSH into your VPS and set up the backend.

```bash
cd ~/unity-presentation/unity-api

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server (for testing)
# It will listen on port 5001
python app.py
```
*Note: For production, consider using Gunicorn/Nginx.*

## 3. Frontend Setup (`unity-ui`)
Open a new terminal session (or use `screen`/`tmux`).

```bash
cd ~/unity-presentation/unity-ui

# Install dependencies
npm install

# Create production config
# Replace YOUR_VPS_IP with the actual IP address of your VPS
echo "VITE_API_URL=http://YOUR_VPS_IP:5001" > .env.production

# Build the project
npm run build

# Serve the build (simple way)
npm run preview -- --host --port 8080
```
The site will be available at `http://YOUR_VPS_IP:8080`.

## 4. Accessing the Site
Open your browser and navigate to:
`http://YOUR_VPS_IP:8080`

Ensure your VPS firewall allows traffic on ports 5001 (API) and 8080 (UI).
