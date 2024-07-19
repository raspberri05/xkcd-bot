# xkcd-bot

## Documentation

This section provides an overview of the `xkcd-bot` functionalities and how to use them.

### Installation

Go to https://discord.com/oauth2/authorize?client_id=1263696260683005972&permissions=18432&integration_type=0&scope=bot to add this bot to your discord server.

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

### Running

```bash
python watcher.py
```
