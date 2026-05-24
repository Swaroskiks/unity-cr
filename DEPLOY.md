# Deployment Guide

Follow these steps to deploy the Unity Project Presentation site on your VPS.

## Prerequisites
- A VPS (Ubuntu/Debian recommended)
- Node.js 20+ installed

## 1. Transfer Files
Copy the entire project folder to your VPS. You can use `scp` or `rsync`.
```bash
# From your local machine
scp -r /path/to/quiz-app user@your-vps-ip:~/unity-presentation
```

## 2. Frontend Setup (`unity-ui`)
Open a new terminal session (or use `screen`/`tmux`).

```bash
cd ~/unity-presentation/unity-ui

# Install dependencies
npm install

# Build the project
npm run build

# Serve the build (simple way)
npm run preview -- --host --port 8080
```
The site will be available at `http://YOUR_VPS_IP:8080`.

## 3. Accessing the Site
Open your browser and navigate to:
`http://YOUR_VPS_IP:8080`

Ensure your VPS firewall allows traffic on port 8080 (UI).
