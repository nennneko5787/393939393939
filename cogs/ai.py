import asyncio

import discord
from discord.ext import commands
from openai import AsyncOpenAI

class AIChatCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = AsyncOpenAI(base_url="https://api.voids.top/v1", api_key="39")
        
    @commands.command()
    async def aichat(self, ctx: commands.Context, *, prompt: str):
        message = await ctx.reply("生成中")
        try:
            stream = await self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
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
        except Exception as e:
            await message.edit(str(e))
            
async def setup(bot: commands.Bot):
    await bot.add_cog(AIChatCog(bot))
        