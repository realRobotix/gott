import disnake, os
from disnake.ext import commands


class Settings(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        super().__init__()


def setup(bot: commands.Bot):
    bot.add_cog(Settings(bot))
