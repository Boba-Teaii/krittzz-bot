import discord
from discord.ext import commands
from discord import app_commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot latency")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)

        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Latency: **{latency}ms**",
            color=0x00ffcc
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Misc(bot))