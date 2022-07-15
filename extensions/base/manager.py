import os
import subprocess
import disnake
import disnake.ext
from disnake.ext import commands
from gott import Gott
from utils.embeds import SubprocessEmbed


class Manager(commands.Cog):
    def __init__(self, bot: Gott) -> None:
        self.bot = bot

    @commands.slash_command(name="manager", description="used to manage extensions")
    @commands.is_owner()
    async def manager(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @manager.sub_command_group(name="extension")
    async def extension(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @extension.sub_command(
        name="load", description='load an extension. use "all" to load all extensions'
    )
    async def load(
        self, inter: disnake.ApplicationCommandInteraction, extension: str
    ) -> None:
        successful_loads = ""
        failed_loads = ""
        if extension == "all":
            for (dirpath, dirname, filenames) in os.walk(f"{self.bot.path}/extensions"):
                for file in filenames:
                    fullPath = os.path.join(dirpath, file)
                    if file.endswith(".py") and not file.startswith("_"):
                        extension = (
                            "extensions."
                            + fullPath[:-3]
                            .replace("/", ".")
                            .replace("\\", ".")
                            .split("extensions.")[1]
                        )
                        if extension.startswith("extensions.base"):
                            continue
                        try:
                            self.bot.load_extension(extension)
                            successful_loads += f"\nsuccessfully loaded {extension}"
                        except Exception as e:
                            failed_loads += f"\nfailed to load {extension}\n{e}"
        else:
            try:
                self.bot.load_extension(f"extensions.{extension}")
                successful_loads += f"\nsuccessfully loaded {extension}"
            except Exception as e:
                failed_loads += f"\nfailed to load {extension}\n{e}"
        embed = self.create_embed(
            successful=successful_loads, failed=failed_loads, type="load"
        )
        await inter.response.send_message(embed=embed, ephemeral=True)

    @extension.sub_command(
        name="unload",
        description='unload an extension. use "all" to unload all extensions',
    )
    async def unload(
        self, inter: disnake.ApplicationCommandInteraction, extension: str
    ) -> None:
        successful_unloads = ""
        failed_unloads = ""
        if extension == "all":
            for extension in list(self.bot.extensions):
                if extension.startswith("extensions.base"):
                    continue
                try:
                    self.bot.unload_extension(extension)
                    successful_unloads += f"\nsuccessfully unloaded {extension}"
                except Exception as e:
                    failed_unloads += f"\nfailed to unload {extension}\n{e}"
        else:
            try:
                self.bot.unload_extension(f"extensions.{extension}")
                successful_unloads += f"\nsuccessfully unloaded {extension}"
            except Exception as e:
                failed_unloads += f"\nfailed to unload {extension}\n{e}"
        embed = self.create_embed(
            successful=successful_unloads, failed=failed_unloads, type="unload"
        )
        await inter.response.send_message(embed=embed, ephemeral=True)

    @extension.sub_command(
        name="reload",
        description='reload an extension. use "all" to reload all extensions',
    )
    async def reload(
        self, inter: disnake.ApplicationCommandInteraction, extension: str
    ) -> None:
        successful_reloads = ""
        failed_reloads = ""
        if extension == "all":
            for extension in list(self.bot.extensions):
                if extension.startswith("extensions.base"):
                    continue
                try:
                    self.bot.reload_extension(extension)
                    successful_reloads += f"\nsuccessfully reloaded {extension}"
                except Exception as e:
                    failed_reloads += f"\nfailed to reload {extension}\n{e}"
        else:
            try:
                self.bot.reload_extension(f"extensions.{extension}")
                successful_reloads += f"\nsuccessfully reloaded {extension}"
            except Exception as e:
                failed_reloads += f"\nfailed to reload {extension}\n{e}"
        embed = self.create_embed(
            successful=successful_reloads, failed=failed_reloads, type="reload"
        )
        await inter.response.send_message(embed=embed, ephemeral=True)

    @extension.sub_command(
        name="list", description="list all currently running extensions"
    )
    async def list(self, inter: disnake.ApplicationCommandInteraction) -> None:
        response = ""
        for key in self.bot.extensions.keys():
            response += key + "\n"
        await inter.response.send_message(response, ephemeral=True)

    def create_embed(self, type: str, successful: str, failed: str) -> disnake.Embed:
        successful = successful.strip()
        failed = failed.strip()
        if successful == "" or failed == None:
            successful = "none"
            colour = disnake.Colour.red()
        if failed == "" or failed == None:
            failed = "none"
            colour = disnake.Colour.green()
        if successful != "none" and failed != "none":
            colour = disnake.Colour.orange()
        embed = disnake.Embed(title=f"Extensions {type}ed!", colour=colour)
        embed.add_field(
            name=f"Successful {type}s:", value=f"```{successful}```", inline=False
        )
        embed.add_field(name=f"Failed {type}s:", value=f"```{failed}```", inline=False)
        return embed

    @manager.sub_command_group(name="service")
    async def service(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @service.sub_command(name="restart")
    async def restart(self, inter: disnake.ApplicationCommandInteraction):
        pro = subprocess.run(
            ["systemctl", "restart", "gott"],
            cwd=self.bot.path,
            capture_output=True,
            encoding="utf-8",
        )
        await inter.response.send_message(embed=SubprocessEmbed(pro), ephemeral=True)

    @manager.sub_command_group(name="git")
    async def git(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @git.sub_command(name="pull")
    async def pull(self, inter: disnake.ApplicationCommandInteraction):
        a = subprocess.run(
            ["git", "pull"], cwd=self.bot.path, capture_output=True, encoding="utf-8"
        )
        await inter.response.send_message(embed=SubprocessEmbed(a), ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Manager(bot))
