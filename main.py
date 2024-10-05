import os

import dotenv
import discord
from discord.ext import commands

dotenv.load_dotenv()

bot = commands.Bot(command_prefix=["39love#", "39❤️#", "h.yummy#"])


@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"Ping: `{bot.latency}`ms")


bot.run(os.getenv("discord"))
