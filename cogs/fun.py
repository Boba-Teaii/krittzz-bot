import discord
from discord.ext import commands
from discord import app_commands
from utils.fonts import transform

# 🔤 Available fonts
FONT_LIST = [
    "bold","italic","script","double","mono",
    "bubble","square","smallcaps","weird","flip",
    "wide","tiny"
]

# 🔽 DROPDOWN
class FontSelect(discord.ui.Select):
    def __init__(self, text, user):
        self.text = text
        self.user = user

        options = [
            discord.SelectOption(label=f, description=f"{f} style")
            for f in FONT_LIST
        ]

        super().__init__(placeholder="🎨 Choose a font", options=options)

    async def callback(self, interaction: discord.Interaction):
        # ❌ block other users
        if interaction.user != self.user:
            return await interaction.response.send_message(
                "❌ Not your interaction", ephemeral=True
            )

        # ✅ prevent interaction failed
        await interaction.response.defer()

        font = self.values[0]
        result = transform(self.text, font)

        # 🧹 delete dropdown message
        try:
            await interaction.message.delete()
        except:
            pass

        # 🚀 send ONLY plain text
        await interaction.followup.send(result)


# 📦 VIEW
class FontView(discord.ui.View):
    def __init__(self, text, user):
        super().__init__(timeout=60)
        self.add_item(FontSelect(text, user))


# 📝 MODAL (text input)
class FontModal(discord.ui.Modal, title="Font Generator"):
    text_input = discord.ui.TextInput(
        label="Enter your text",
        placeholder="Type something cool...",
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "🎨 Choose your font:",
            view=FontView(self.text_input.value, interaction.user),
            ephemeral=True  # only user sees dropdown
        )


# ⚙️ COG
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="font_change", description="Generate fancy fonts")
    async def font_change(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FontModal())


# 🔌 LOAD
async def setup(bot):
    await bot.add_cog(Fun(bot))