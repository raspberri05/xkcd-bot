# xkcd-bot

## Documentation

This section provides an overview of the `xkcd-bot` functionalities and how to use them.

### Installation

Go to the below link to add this bot to your discord server

https://discord.com/oauth2/authorize?client_id=1263696260683005972&permissions=18432&integration_type=0&scope=bot 

### Commands

- **latest**: Fetches the latest xkcd comic and sends it in the chat.
  - Usage: `/latest`
  
- **get**: Fetches a specific xkcd comic by its number and sends it in the chat.
  - Usage: `/get <number>`
    - `<number>`: The number of the xkcd comic to fetch.
  
- **random**: Fetches a random xkcd comic and sends it in the chat.
  - Usage: `/random`

## Getting Started

### Installation

```bash
pip install -r src/requirements.txt -r requirements-dev.txt
```

### Setup

1. Create a new discord app [here](https://discord.com/developers/applications)
2. Go to the bot tab and enable message intent
3. Go to the Oauth2 tab, select ```bot``` scope, then select ```send messages``` and ```embed links``` in bot permissions
4. Copy the url at the bottom of the Oauth2 tab and paste it into your web browser to add the bot to a server
5. Go to the bot tab, find the token, and create ```.env``` at the repository root, and add ```DISCORD_TOKEN=your_token-here```

### Running

```bash
python watcher.py
```

*This project uses pymon to automatically restart the server on file changes*
