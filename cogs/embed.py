import discord
from discord.ext import commands
from discord import app_commands

class EmbedModal(discord.ui.Modal, title="Create Embed"):
    title_input = discord.ui.TextInput(label="Title", required=False)
    desc = discord.ui.TextInput(label="Description", style=discord.TextStyle.long)
    footer = discord.ui.TextInput(label="Footer", required=False)

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=self.title_input.value,
            description=self.desc.value,
            color=0x2f3136
        )

        if self.footer.value:
            embed.set_footer(text=self.footer.value)

        await interaction.response.send_message(embed=embed)

class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="embed_create", description="Create embed")
    async def embed_create(self, interaction: discord.Interaction):
        await interaction.response.send_modal(EmbedModal())

async def setup(bot):
    await bot.add_cog(EmbedCog(bot))