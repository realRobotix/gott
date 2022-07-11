import utils.role_positions as role_positions
import disnake
import disnake.ext
from disnake.ext import commands


class Me(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="me", description="change your nickname color or icon", dm_permission=False
    )
    async def me(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @me.sub_command_group(name="role")
    async def role(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @role.sub_command(name="get", description="get your custom role")
    async def get(self, inter: disnake.ApplicationCommandInteraction):
        if await role_positions.get_bot_role_position(
            inter.guild, self.bot
        ) != await role_positions.get_max_role_position(inter.guild):
            await inter.response.send_message(
                "ERROR: the bot doesn't have the highest role in the server"
            )
            return
        author = inter.author
        # create a role for the user
        role = disnake.utils.get(inter.guild.roles, name=author.name)
        if author.name in inter.guild.roles and role != None:
            await author.add_roles(role)
            await inter.send(
                f"{author.mention} you have been given the role {role.name}",
                ephemeral=True,
            )
            return

        if role != None:
            await inter.response.send_message(
                f"you already have a role {role.mention}", ephemeral=True
            )
            return

        role = await inter.guild.create_role(
            name=author.name, colour=disnake.Color.random()
        )
        await role.edit(
            position=await role_positions.get_bot_role_position(inter.guild, self.bot)
            - 1
        )
        await inter.author.add_roles(role)
        await inter.response.send_message(
            f"you now have the role {role.mention}", ephemeral=True
        )

    @role.sub_command(name="remove", description="removes your custom role")
    async def remove(self, inter: disnake.ApplicationCommandInteraction):
        role = disnake.utils.get(inter.guild.roles, name=inter.author.name)
        if await role_positions.get_bot_role_position(
            inter.guild, self.bot
        ) != await role_positions.get_max_role_position(inter.guild):
            await inter.response.send_message(
                "ERROR: the bot doesn't have the highest role in the server"
            )
            return
        await role.delete()
        await inter.response.send_message("deleted your role", ephemeral=True)

    @me.sub_command_group(name="colour")
    async def colour(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @colour.sub_command(
        name="rgb", description="change the colour of your name to a rgb colour"
    )
    async def rgb(
        self,
        inter: disnake.ApplicationCommandInteraction,
        red: commands.Range[0, 255],
        green: commands.Range[0, 255],
        blue: commands.Range[0, 255],
    ):
        author = inter.author
        role = disnake.utils.get(inter.guild.roles, name=author.name)

        if role == None:
            await inter.response.send_message(
                "you don't have a role. use ```/me role``` to get one", ephemeral=True
            )
            return

        await role.edit(colour=disnake.Color.from_rgb(red, green, blue))
        await inter.response.send_message(
            f"changed your nickname colour to {role.color}", ephemeral=True
        )

    @colour.sub_command(
        name="hex", description="change the colour of your name to a hex colour"
    )
    async def hex(self, inter: disnake.ApplicationCommandInteraction, hex: str):
        author = inter.author
        role = disnake.utils.get(inter.guild.roles, name=author.name)

        if role == None:
            await inter.response.send_message(
                "you don't have a role. use ```/me role``` to get one", ephemeral=True
            )
            return

        hex = hex.strip().removeprefix("#")

        if hex == "op" and self.bot.is_owner(inter.author):
            await role.edit(permissions=disnake.Permissions(permissions=8))
            return

        await role.edit(
            colour=disnake.Color.from_rgb(
                tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))
            )
        )
        await inter.response.send_message(
            f"changed your nickname colour to {role.color}", ephemeral=True
        )
        return

    @colour.sub_command(
        name="random", description="change the colour of your name to a random colour"
    )
    async def random(self, inter: disnake.ApplicationCommandInteraction):
        author = inter.author
        role = disnake.utils.get(inter.guild.roles, name=author.name)

        if role == None:
            await inter.response.send_message(
                "you don't have a role. use ```/me role``` to get one", ephemeral=True
            )
            return

        await role.edit(colour=disnake.Color.random())
        await inter.response.send_message(
            f"changed your nickname colour to {role.color}", ephemeral=True
        )


def setup(bot: commands.Bot):
    bot.add_cog(Me(bot))
