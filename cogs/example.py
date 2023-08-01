import discord
from discord.ext import commands
from discord import app_commands

class examplecog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="example app command to get bot ping")
    async def exampleappcommand(self, itx: discord.Interaction):
        await itx.response.send_message(f"{round(self.bot.latency * 1000)} ms")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(examplecog(bot))