import os
import discord

# Bot Configuration
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", "")

# Discord Intents - Bot needs all intents for full functionality
INTENTS = discord.Intents.all()

# Authorized roles that can use the announce command
AUTHORIZED_ROLES = ["Founder 👑", "Co-Founder 👑"]

# Bot settings
COMMAND_PREFIX = "!"
ANNOUNCEMENT_SIGNATURE = "— Team VDL Official"

# Limits
MAX_ANNOUNCEMENT_LENGTH = 2000
MAX_ROLES_IN_DROPDOWN = 25
UI_TIMEOUT = 60  # seconds
