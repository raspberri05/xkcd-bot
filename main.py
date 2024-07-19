import os
from discord import Intents
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.hybrid_command()
async def test(ctx):
    await ctx.send("testing123")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    await bot.tree.sync()
    print("Command tree synced.")


bot.run(TOKEN)
