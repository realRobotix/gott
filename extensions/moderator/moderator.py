import disnake
from disnake.ext import commands
import re


class Moderator(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(name="moderator")
    async def moderator(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @moderator.sub_command_group(name="messages")
    async def messages(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @messages.sub_command(name="delete")
    @commands.has_permissions(manage_messages=True)
    async def delete(
        self,
        inter: disnake.ApplicationCommandInteraction,
        limit: int,
        member: disnake.Member = None,
        regex: str = None,
    ):
        if regex != None:
            pattern = re.compile(regex)

        def check(m: disnake.Message):
            if member != None and regex != None:
                return m.author == member and re.search(pattern, m.content)
            if member != None or regex != None:
                return m.author == member or re.search(pattern, m.content)

        await inter.response.defer(ephemeral=True)
        deleted = await inter.channel.purge(limit=limit, check=check)
        await inter.edit_original_message(content=f"deleted {len(deleted)} messages")


def setup(bot: commands.Bot):
    bot.add_cog(Moderator(bot))
