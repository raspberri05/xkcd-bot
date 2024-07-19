# xkcd-bot

## Documentation

This section provides an overview of the `xkcd-bot` functionalities and how to use them.

### Commands

- **latest**: Fetches the latest xkcd comic and sends it in the chat.
  - Usage: `/latest`
  
- **get**: Fetches a specific xkcd comic by its number and sends it in the chat.
  - Usage: `/get <number>`
    - `<number>`: The number of the xkcd comic to fetch.
  
- **random**: Fetches a random xkcd comic and sends it in the chat.
  - Usage: `/random`

### Events

- **on_ready**: Event handler for when the bot has successfully connected to Discord. Indicates that the bot is online and ready to receive commands.

## Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Setup

### Running

```bash
python src/main.py
```
