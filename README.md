# Discord Channel Merge Bot

This bot helps you move messages from one Discord channel to another. It provides admin commands to move all messages, specific messages within a timeframe, or messages from specific users.

You can also join our NIM community on Discord, Reddit, and Facebook, or visit our homepage:

[![Join our Discord](https://img.shields.io/badge/Discord-Join-blue)](https://discord.com/invite/SVYMhKpCAb)
[![Visit our Homepage](https://img.shields.io/badge/Homepage-Visit-orange)](https://nimiates.org)
[![Visit our Reddit](https://img.shields.io/badge/Reddit-Visit-red)](https://www.reddit.com/r/nimiates/)
[![Visit our Facebook](https://img.shields.io/badge/Facebook-Visit-blue)](https://www.facebook.com/groups/nimiates/)

## Features

- Move all messages from one channel to another.
- Move the last 'X' days of messages.
- Move messages from specific users.
- User-friendly command system.

## Commands
The bot provides commands to move messages between channels. Here's how to use them:

`!move #Channel-x #Channel-y`: Moves all messages from Channel-x to Channel-y. This is the default action if no additional parameters are provided.

`!move #Channel-x #Channel-y -last "7 days"`: Moves messages from Channel-x to Channel-y that were sent in the last specified time period (e.g., "7 days" or "1 hour").

`!move #Channel-x #Channel-y -from_user @username`: Moves all messages sent by a specific user from Channel-x to Channel-y.

## Parameters
`#Channel-x`: Mention of the source channel where messages will be moved from.
`#Channel-y`: Mention of the destination channel where messages will be moved to.
`-last "<time_period>"`: (Optional) The time period for which messages will be moved, specified in quotes. Replace <time_period> with a value like "7 days" or "1 hour".
`-from_user @username`: (Optional) The mention of the user whose messages will be moved. Replace @username with the actual user mention.

## Examples
To move all messages from one channel to another:
`!move #source-channel #destination-channel`

To move messages from the last 7 days:
`!move #source-channel #destination-channel -last "7 days"`

To move messages from a specific user:
`!move #source-channel #destination-channel -from_user @User`

Please replace #source-channel and #destination-channel with the actual channel mentions, and @User with the mention of the user whose messages you want to move.

## Requirements

- Python 3.8 or higher
- Discord API Token
- Discord.py library

## Installation

### Prerequisites

1. **Install Python**: Make sure Python is installed on your system. You can download it from [Python.org](https://www.python.org/downloads/).

2. **Install pip**: Pip is the package installer for Python. It is usually included in Python installations.

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Nimiates/discord-channel-merge-bot.git
   
2. **Change to the project directory**:

`cd discord-channel-merge-bot`

3. **Create a virtual environment**:

`python -m venv venv`

5. **Activate the virtual environment**:

*Windows*:

`venv\Scripts\activate`

*MacOS/Linux*:

`source venv/bin/activate`

5. **Install the dependencies**:

`pip install -r requirements.txt`

### Configuration

1. **Create a `.env` file** in the project directory to store your environment variables:

`DISCORD_TOKEN=your_discord_bot_token_here`

`BOT_OWNER_ID=your_discord_user_id_here`

`DISCORD_PREFIX=!`

2. **Replace the placeholder values with your actual values**.

## Running the Bot

1. **Start the bot**:

`python discord_move_bot.py`

2. **Stop the bot**: To stop the bot, press Ctrl+C in the terminal where it is running.

### More Information
To learn more about running and managing Discord bots, read the official [Discord.py documentation](https://discordpy.readthedocs.io/en/stable/#getting-started).

Join our NIM community on Discord, Reddit, and Facebook, or visit our homepage:

[![Join our Discord](https://img.shields.io/badge/Discord-Join-blue)](https://discord.com/invite/SVYMhKpCAb)
[![Visit our Homepage](https://img.shields.io/badge/Homepage-Visit-orange)](https://nimiates.org)
[![Visit our Reddit](https://img.shields.io/badge/Reddit-Visit-red)](https://www.reddit.com/r/nimiates/)
[![Visit our Facebook](https://img.shields.io/badge/Facebook-Visit-blue)](https://www.facebook.com/groups/nimiates/)

## License
This project is licensed under the MIT License.
