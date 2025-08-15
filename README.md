# Discord Announcement Bot

A Discord bot for sending role-mentioned announcements with image support and permission controls.

## Features

- **Slash Command Interface**: Use `/announce` to create announcements
- **Role-Based Permissions**: Only users with "Founder 👑" or "Co-Founder 👑" roles can use the bot
- **Interactive Role Selection**: Choose which roles to mention via dropdown menu
- **Rich Content Support**:
  - Text announcements with automatic signature
  - Optional image URLs with embed display
  - File attachment support for images
- **Error Handling**: Comprehensive error handling for all edge cases
- **Security**: Proper permission checks and input validation

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- A Discord bot token
- discord.py library

### Installation

1. **Clone or download this project**

2. **Install dependencies**:
   ```bash
   pip install discord.py
   ```

3. **Set up environment variables**:
   
   Create a `.env` file or set the environment variable:
   ```bash
   export DISCORD_BOT_TOKEN="your_bot_token_here"
   ```

4. **Configure your Discord bot**:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application and bot
   - Copy the bot token
   - Enable the following bot permissions:
     - Send Messages
     - Use Slash Commands
     - Embed Links
     - Attach Files
     - Mention Everyone
     - Read Message History

5. **Invite the bot to your server**:
   - Generate an invite URL with the required permissions
   - Make sure the bot has a role higher than the roles it needs to mention

### Running the Bot Locally

```bash
python main.py
```

## Free Hosting on Railway.app

### Prerequisites for Railway Deployment

1. **GitHub Account** - Create one at https://github.com if you don't have one
2. **Railway Account** - Sign up at https://railway.app using your GitHub account
3. **Discord Bot Token** - From Discord Developer Portal

### Step-by-Step Deployment Guide

#### Step 1: Upload Code to GitHub

1. **Download your project** as a ZIP file from Replit
2. **Extract the ZIP** file on your computer
3. **Create a new repository** on GitHub:
   - Go to https://github.com
   - Click "New repository"
   - Name it: `discord-announcement-bot`
   - Set it to Public
   - Don't initialize with README (we already have one)
   - Click "Create repository"

4. **Upload your code**:
   - Click "uploading an existing file"
   - Drag and drop all files from the extracted folder
   - **Important**: Do NOT upload `.env` files or any files with tokens
   - Write commit message: "Initial bot code"
   - Click "Commit changes"

#### Step 2: Deploy on Railway

1. **Go to Railway.app** and sign in with GitHub
2. **Click "New Project"**
3. **Select "Deploy from GitHub repo"**
4. **Choose your `discord-announcement-bot` repository**
5. **Railway will automatically detect it's a Python project**

#### Step 3: Configure Environment Variables

1. **In Railway dashboard**, click on your project
2. **Go to "Variables" tab**
3. **Add new variable**:
   - Name: `DISCORD_BOT_TOKEN`
   - Value: Your Discord bot token (paste it here)
4. **Click "Add"**

#### Step 4: Deploy

1. **Railway will automatically deploy** your bot
2. **Check the "Deployments" tab** for status
3. **Check "Logs" tab** to see if bot connected successfully
4. **Look for**: ✅ Bot logged in as [YourBotName]

Your bot is now hosted for free and will run 24/7!
