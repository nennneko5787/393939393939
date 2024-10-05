import os

import dotenv
import discord
from discord.ext import commands

dotenv.load_dotenv()

bot = commands.Bot(command_prefix=["39love#", "lenlove#", "h.yummy#"])

@bot.event
async def setup_hook():
    await bot.load_extension("cogs.ai")

@bot.command()
async def delete(ctx: commands.Context, msgId: int):
    await ctx.channel.get_message(msgId).delete()
    await ctx.reply("success")

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"Ping: `{bot.latency}`ms")


bot.run(os.getenv("discord"))
