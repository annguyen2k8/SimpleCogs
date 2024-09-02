import discord
from discord import app_commands
from discord.ext import commands

class SimpleCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(message: discord.Message) -> None:
        if message.author.bot:
            return
        
        if 'simp' in message.content.lower():
            await message.add_reaction('regional_indicator_s')
            await message.add_reaction('regional_indicator_i')
            await message.add_reaction('regional_indicator_m')
            await message.add_reaction('regional_indicator_p')

async def main(bot: commands.Bot) -> None:
    await bot.add_cog(SimpleCog(bot))