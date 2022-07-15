import disnake
from disnake.ext import commands
import subprocess
from manager import SubprocessEmbed


class GitCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.is_owner()
    @commands.slash_command(name="git")
    async def git(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @git.sub_command(name="pull")
    async def pull(self, inter: disnake.ApplicationCommandInteraction):
        a = subprocess.run("git pull", capture_output=True, encoding="utf-8")
        await inter.response.send_message(embed=SubprocessEmbed(a))


def setup(bot: commands.Bot):
    bot.add_cog(GitCommand(bot))
