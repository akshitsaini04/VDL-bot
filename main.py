import os
import asyncio
from discord.ext import commands
import discord
from config import BOT_TOKEN, INTENTS
from bot.commands import setup_commands

def main():
    """Main entry point for the Discord bot."""
    if not BOT_TOKEN:
        print("❌ Error: DISCORD_BOT_TOKEN environment variable not set!")
        print("Please set your Discord bot token in the environment variables.")
        return
    
    # Create bot instance
    bot = commands.Bot(command_prefix="!", intents=INTENTS)
    
    # Setup commands
    setup_commands(bot)
    
    # Bot ready event
    @bot.event
    async def on_ready():
        print(f"✅ Bot logged in as {bot.user}")
        try:
            synced = await bot.tree.sync()
            print(f"🔹 Synced {len(synced)} slash commands.")
        except Exception as e:
            print(f"❌ Error syncing commands: {e}")
    
    # Run the bot
    try:
        bot.run(BOT_TOKEN)
    except discord.LoginFailure:
        print("❌ Error: Invalid Discord bot token!")
    except Exception as e:
        print(f"❌ Error starting bot: {e}")

if __name__ == "__main__":
    main()
