import disnake, os
from disnake.ext import commands


class BotEmoji(commands.Cog):
    def __init__(self, bot: commands.bot) -> None:
        self.bot = bot

    @commands.slash_command(name="emoji")
    async def emoji(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @emoji.sub_command(name="update")
    async def update(self, inter: disnake.ApplicationCommandInteraction) -> None:
        failed = ""
        # await inter.response.defer(with_message=True, ephemeral=True)
        # await inter.response.send_message(content="updating emojis ...", ephemeral=True)
        for (dirpath, dirname, filenames) in os.walk("./resources/emoji"):
            for file in filenames:
                try:
                    fullPath = os.path.join(dirpath, file)
                    if file.endswith((".png", ".jpg")) and not file.startswith(
                        ("_", ".")
                    ):
                        await inter.guild.create_custom_emoji(
                            name=self.bot.user.name + "_" + file.split(".")[0],
                            image=open(file=fullPath, mode="rb").read(),
                        )
                except Exception as e:
                    failed += f"{e}"
        if failed == "":
            await inter.response.send_message(
                content="updated all bot emojis", ephemeral=True
            )
            return
        else:
            await inter.response.send_message(
                content=f"ERROR:\n{failed}", ephemeral=True
            )
            return


def setup(bot: commands.Bot):
    bot.add_cog(BotEmoji(bot))
