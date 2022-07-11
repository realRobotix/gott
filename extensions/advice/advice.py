import disnake
from disnake.ext import commands
from requests import request


class Advice(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.uri = "https://api.adviceslip.com/advice"

    @commands.slash_command(name="advice")
    async def advice(
        self, inter: disnake.ApplicationCommandInteraction, search: str = None
    ):
        if search != None:
            advice: dict = request("GET", self.uri + "/search/" + search).json()
            if "message" in advice.keys():
                await inter.response.send_message(content=advice["message"]["text"])
                return
            await inter.response.send_message(
                embed=SearchEmbed(search=search, advice=advice)
            )
            return

        advice: dict = request("GET", self.uri).json()
        if "message" in advice.keys():
            await inter.response.send_message(content=advice["message"]["text"])
            return
        await inter.response.send_message(content=advice["slip"]["advice"])


class SearchEmbed(disnake.Embed):
    def __init__(self, search: str, advice: dict):
        super().__init__(title=f"Advice Search: {search}")
        for slip in advice["slips"][:24]:
            self.add_field(
                name="Advice No. " + str(slip["id"]) + ":", value=slip["advice"]
            )


def setup(bot: commands.Bot):
    bot.add_cog(Advice(bot))
