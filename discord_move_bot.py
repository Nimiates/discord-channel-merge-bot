import os
import discord
from discord.ext import commands
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Get the bot token from the environment variables
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.command(name='move')
async def move_messages(ctx, channel_from: discord.TextChannel, channel_to: discord.TextChannel, action: str = '-all', time_period: str = None, user: discord.User = None):
    """
    Moves messages from one channel to another based on user command.

    Arguments:
    - channel_from: The source channel to move messages from.
    - channel_to: The target channel to move messages to.
    - action: The action to perform. Options are "-all", "-last <xy-time>", "-from_user".
    - time_period: The time period for "-last" action (e.g., "7 days", "1 hour").
    - user: The user to filter messages for the "-from_user" action.
    """
    if action not in ['-all', '-last', '-from_user']:
        await ctx.send("Invalid action. Use '-all', '-last <xy-time>', or '-from_user'.")
        return

    messages = []
    async for message in channel_from.history(limit=None):
        if action == '-all':
            messages.append(message)
        elif action == '-last':
            if not time_period:
                await ctx.send("Please specify a time period for '-last'.")
                return
            try:
                number, unit = time_period.split()
                number = int(number)
                delta = timedelta(**{unit: number})
            except (ValueError, KeyError):
                await ctx.send("Invalid time period format. Use '<number> days' or '<number> hours'.")
                return

            if datetime.now() - message.created_at <= delta:
                messages.append(message)
        elif action == '-from_user' and user and message.author == user:
            messages.append(message)

    for message in reversed(messages):  # Reversed to maintain order when sending
        attachments = [await attachment.to_file() for attachment in message.attachments]
        await channel_to.send(content=f"{message.author.display_name}: {message.content}", files=attachments)
        await message.delete()

    await ctx.send(f"Moved {len(messages)} messages from {channel_from.name} to {channel_to.name}.")

bot.run(TOKEN)
