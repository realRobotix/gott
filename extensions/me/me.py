import utils.role_positions as role_positions
import disnake
import disnake.ext
from disnake.ext import commands


class Me(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="me", description="change your nickname color or icon", dm_permission=False)
    async def me(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @me.sub_command(name="role", description="get your role")
    async def me_get_role(self, inter: disnake.ApplicationCommandInteraction):
        author = inter.author
        # create a role for the user
        role = disnake.utils.get(inter.guild.roles, name=author.name)
        if author.disnake.Member.roles in role and role != None:
            await author.add_roles(role)
            await inter.send(f"{author.mention} you have been given the role {role.name}")
            return

        if role != None:
            await inter.response.send_message(f"you already have a role {role.mention}")
            return

        if await role_positions.get_bot_role_position(inter.guild, self.bot) != await role_positions.get_max_role_position(inter.guild):
            await inter.response.send_message(f"the bot doesn't have the highest role in the server")
            return

        role = await inter.guild.create_role(name=author.name, colour=disnake.Color.random())
        await role.edit(position=await role_positions.get_bot_role_position(inter.guild, self.bot) - 1)
        await inter.author.add_roles(role)
        await inter.response.send_message(f"you now have the role {role.mention}")

    @me.sub_command(name="colour", description="change the colour of your nickname")
    async def me_change_colour_from_rgb(self, inter: disnake.ApplicationCommandInteraction, red: commands.Range[0, 255] = None, green: commands.Range[0, 255] = None, blue: commands.Range[0, 255] = None, hex: str = None, random: bool = False):
        author = inter.author
        role = disnake.utils.get(inter.guild.roles, name=author.name)

        if role == None:
            await inter.response.send_message("you don't have a role. use ```/me role``` to get one")
            return
        if hex != None:
            await role.edit(colour=disnake.Color.from_rgb(tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))))
            await inter.response.send_message(f"changed your nickname colour to {role.color}")
            return
        if random:
            await role.edit(colour=disnake.Color.random())
            await inter.response.send_message(f"changed your nickname colour to {role.color}")
            return
        if red != None and green != None and blue != None:
            await role.edit(colour=disnake.Color.from_rgb(red, green, blue))
            await inter.response.send_message(f"changed your nickname colour to {role.color}")
            return
        await inter.response.send_message("you need to specify a colour")


def setup(bot: commands.Bot):
    bot.add_cog(Me(bot))
