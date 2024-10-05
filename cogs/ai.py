
import asyncio

import discord
from discord.ext import commands
from openai import AsyncOpenAI

class AIChatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = AsyncOpenAI(base_url="https://api.voids.top/v1", api_key="39")
        self.talkHistory: dict<int, list<dict<str, str>>> = {}
        
    @commands.command()
    async def aichat(self, ctx: commands.Context, *, prompt: str):
        if ctx.author.id != 1048448686914551879:
            return
        if not ctx.author.id in self.talkHistory:
            self.talkHistory[ctx.author.id] = []
            
        self.talkHistory[ctx.author.id].append(
            {
                "role": "user",
                "content": prompt,
            }
        )
        message = await ctx.reply("生成中")
        try:
            stream = await self.client.chat.completions.create(
                messages=self.talkHistory[ctx.author.id],
                model="gemini-1.5-pro-exp-0827",
                stream=True,
            )
            content = ""
            async for chunk in stream:
                try:
                    content = content + (chunk.choices[0].delta.content or "")
                    message = await message.edit(content)
                except:
                    pass
                await asyncio.sleep(0.3)
            self.talkHistory[ctx.author.id].append(
                {
                    "role": "system",
                    "content": content,
            )
        except Exception as e:
            await message.edit(str(e))
            
async def setup(bot: commands.Bot):
    await bot.add_cog(AIChatCog(bot))
        