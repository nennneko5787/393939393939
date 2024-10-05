import discord
from discord.ext import commands
from openai import AsyncClient

class AIChatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = AsyncOpenAI(base_url="https://api.voids.top/v1")
        
    @commands.command()
    async def aichat(ctx: commands.Context):
        pass