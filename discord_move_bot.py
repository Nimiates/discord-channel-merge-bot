import discord
from discord.ext import commands
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
async def move(ctx, action: str, timeframe: str = None, user: discord.User = None, src_channel: discord.TextChannel = None, dest_channel: discord.TextChannel = None):
    if not src_channel or not dest_channel:
        await ctx.send("Please specify both source and destination channels.")
        return

    if action == "-all":
        await move_all_messages(ctx, src_channel, dest_channel, user)
    elif action == "-last":
        await move_last_messages(ctx, timeframe, src_channel, dest_channel, user)
    elif action == "-from_user" and user:
        await move_from_user(ctx, src_channel, dest_channel, user)
    else:
        await ctx.send("Invalid command. Please use '-all', '-last' followed by a timeframe, or '-from_user' followed by a user.")

async def move_all_messages(ctx, src_channel, dest_channel, user):
    messages = await fetch_messages(src_channel, user)
    await move_messages(ctx, messages, dest_channel)

async def move_last_messages(ctx, timeframe, src_channel, dest_channel, user):
    try:
        days = int(timeframe)
        cutoff_date = datetime.now() - timedelta(days=days)
        messages = await fetch_messages(src_channel, user, cutoff_date)
        await move_messages(ctx, messages, dest_channel)
    except ValueError:
        await ctx.send("Please provide a valid number of days for the timeframe.")

async def move_from_user(ctx, src_channel, dest_channel, user):
    messages = await fetch_messages(src_channel, user)
    await move_messages(ctx, messages, dest_channel)

async def fetch_messages(channel, user=None, after_date=None):
    def check_user(msg):
        return not user or msg.author == user

    messages = []
    async for msg in channel.history(limit=None, after=after_date):
        if check_user(msg):
            messages.append(msg)
    return messages

async def move_messages(ctx, messages, dest_channel):
    if not messages:
        await ctx.send("No messages to move.")
        return

    for msg in messages:
        try:
            await dest_channel.send(f"**{msg.author}:** {msg.content}")
            await msg.delete()
        except Exception as e:
            await ctx.send(f"Failed to move a message: {e}")

    await ctx.send(f"Moved {len(messages)} messages to {dest_channel.name}.")

bot.run("YOUR_BOT_TOKEN")
