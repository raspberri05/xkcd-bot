import os
from discord import Intents
from dotenv import load_dotenv
from discord.ext import commands
from lib.scrape import get_latest_num

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.hybrid_command()
async def latest(ctx):
    await ctx.send("fetching latest xkcd comic...")


@bot.hybrid_command()
async def get(ctx, number):
    await ctx.send(f"fetching xkcd comic {number}...")


@bot.hybrid_command()
async def random(ctx):
    await ctx.send("fetching random xkcd comic...")


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord!")
    await bot.tree.sync()
    print("command tree synced.")


bot.run(TOKEN)
