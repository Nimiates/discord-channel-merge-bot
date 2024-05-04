# Discord Channel Merge Bot

This bot helps you move messages from one Discord channel to another. It provides admin commands to move all messages, specific messages within a timeframe, or messages from specific users.

## Features

- Move all messages from one channel to another.
- Move the last 'X' days of messages.
- Move messages from specific users.
- User-friendly command system.

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
   git clone https://github.com/your-username/discord-channel-merge-bot.git
   
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
To learn more about running and managing Discord bots, read the official Discord.py documentation.

## License
This project is licensed under the MIT License.
