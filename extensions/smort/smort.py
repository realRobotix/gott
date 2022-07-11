from time import time
import disnake, wikipedia
from disnake.ext import commands
from time import sleep


class Smort(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="smort", description="answers with a random wikipedia summary"
    )
    async def smort(self, inter: disnake.ApplicationCommandInteraction):
        wikipedia.BeautifulSoup(features="html.parser")
        # TODO: Get lang from db
        wikipedia.set_lang("de")
        response = ""
        while response == "":
            try:
                response = wikipedia.summary(wikipedia.random()).replace("\n", " ")
            except (
                wikipedia.DisambiguationError,
                wikipedia.PageError,
                wikipedia.RedirectError,
                wikipedia.WikipediaException,
            ):
                sleep(1)
        await inter.response.send_message(response)


def setup(bot: commands.Bot):
    bot.add_cog(Smort(bot))
