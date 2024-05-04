# Discord Channel Merge Bot

## Overview

The Discord Channel Merge Bot is a custom Python bot designed to facilitate the merging of messages between two Discord channels. This tool allows administrators to seamlessly move content from one channel to another based on specific criteria, such as time range or user.

## Features

- **Move All Messages**: Transfer all messages from the source channel to the target channel.
- **Move Last X Days**: Move messages from the last specified number of days.
- **Move by User**: Move messages from a specific user.
- **User-Friendly Commands**: Interact with the bot using straightforward commands.

## Commands

The bot offers the following commands:

- `!move -all -Channel-x -Channel-y`: Move all messages from Channel-x to Channel-y.
- `!move -last <number_of_days> -Channel-x -Channel-y`: Move messages from the last specified number of days from Channel-x to Channel-y.
- `!move -from_user <username> -Channel-x -Channel-y`: Move messages from a specific user in Channel-x to Channel-y.

## Requirements

- Python 3.x
- `discord.py` library

## Usage

1. Install the required dependencies:

    ```bash
    pip install discord.py
    ```

2. Replace `YOUR_BOT_TOKEN` in the code with your actual bot token.

3. Run the bot:

    ```bash
    python discord_move_bot.py
    ```

## License

This project is open-source and licensed under the [MIT License](LICENSE).

## Contributing

If you wish to contribute to this project, please submit a pull request or open an issue. All contributions are welcome!
