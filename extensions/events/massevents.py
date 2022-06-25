import datetime
import disnake
from disnake import TextInputStyle, ui
import disnake.ext
from disnake.ext import commands


class Massevents(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command()
    async def massevents(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @massevents.sub_command()
    async def create(self, inter: disnake.ApplicationCommandInteraction):
        inter.response.send_modal(
            ui.Modal(
                title="New Massevent",
                custom_id="massevent_modal",
                timeout=6000,
                components=(
                    ui.TextInput(label="Name"),
                    ui.TextInput(label="Description"),
                    ui.TextInput(label="Image-URL"),
                    ui.ActionRow(
                        ui.TextInput(label="Date", placeholder="2022-06-25"),
                        ui.TextInput(label="Start Time", placeholder="10:24"),
                        ui.TextInput(label="End Time", placeholder="21:45"),
                    ),
                    ui.ActionRow(
                        ui.TextInput(label="Date", placeholder="2020-11-12"),
                        ui.TextInput(label="Start Time", placeholder="14:43"),
                        ui.TextInput(label="End Time", placeholder="18:35"),
                    ),
                    ui.ActionRow(
                        ui.TextInput(
                            label="Date", placeholder="2021-04-23", required=False
                        ),
                        ui.TextInput(
                            label="Start Time", placeholder="16:32", required=False
                        ),
                        ui.TextInput(
                            label="End Time", placeholder="17:55", required=False
                        ),
                    ),
                    ui.ActionRow(
                        ui.TextInput(
                            label="Date", placeholder="2019-12-24", required=False
                        ),
                        ui.TextInput(
                            label="Start Time", placeholder="11:13", required=False
                        ),
                        ui.TextInput(
                            label="End Time", placeholder="13:35", required=False
                        ),
                    ),
                    ui.ActionRow(
                        ui.TextInput(
                            label="Date", placeholder="2020-07-21", required=False
                        ),
                        ui.TextInput(
                            label="Start Time", placeholder="12:53", required=False
                        ),
                        ui.TextInput(
                            label="End Time", placeholder="14:05", required=False
                        ),
                    ),
                ),
            )
        )
        return


def setup(bot: commands.Bot):
    bot.add_cog(Massevents(bot))
