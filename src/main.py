import os
from discord import Intents
from dotenv import load_dotenv
from discord.ext import commands
from discord import Embed
from lib.scrape import get_random, get_latest, get_specific

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.hybrid_command()
async def latest(ctx):
    try:
        link = get_latest()
        embed = Embed(title=link[2], url=link[1])
        embed.set_image(url=link[0])
        embed.set_footer(text=link[3])
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(
            "failed to retrieve latest xkcd comic. please contact the developer if this issue persists"
        )


@bot.hybrid_command()
async def get(ctx, number):
    try:
        link = get_specific(number)
        embed = Embed(title=link[2], url=link[1])
        embed.set_image(url=link[0])
        embed.set_footer(text=link[3])
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(
            "failed to retrieve specified xkcd comic. please contact the developer if this issue persists"
        )


@bot.hybrid_command()
async def random(ctx):
    try:
        link = get_random()
        embed = Embed(title=link[2], url=link[1])
        embed.set_image(url=link[0])
        embed.set_footer(text=link[3])
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(
            "failed to retrieve random xkcd comic. please contact the developer if this issue persists"
        )


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord!")
    await bot.tree.sync()
    print("command tree synced.")


bot.run(TOKEN)
