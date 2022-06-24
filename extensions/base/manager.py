import os
import disnake
import disnake.ext
from disnake.ext import commands


class Manager(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="manager", description="used to manage extensions")
    @commands.is_owner()
    async def manager(self, inter: disnake.ApplicationCommandInteraction):
        pass

    @manager.sub_command(name="load", description="load an extension. use \"all\" to load all extensions")
    async def extensions_load(self, inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
        if extension == "all":
            for (dirpath, dirname, filenames) in os.walk("./extensions"):
                successful_loads = ""
                failed_loads = ""
                for file in filenames:
                    if dirname == "base":
                        continue
                    fullPath = os.path.join(dirpath, file)
                    if file.endswith(".py") and not file.startswith("_"):
                        extension = "extensions." + fullPath[:-
                                                             3].replace("/", ".").replace("\\", ".").split("extensions.")[1]
                        try:
                            self.bot.load_extension(extension)
                            successful_loads += f"loaded {extension}\n"
                        except Exception as e:
                            failed_loads += f"failed to load {extension}\n{e}\n"
                if successful_loads != "":
                    await inter.response.send_message(successful_loads, ephemeral=True)
                if failed_loads != "":
                    await inter.response.send_message(failed_loads, ephemeral=True)
            return
        try:
            self.bot.load_extension(f"extensions.{extension}")
            await inter.response.send_message(f"loaded {extension}", ephemeral=True)
        except Exception as e:
            await inter.response.send_message(f"failed to load {extension}\n{e}", ephemeral=True)

    @manager.sub_command(name="unload", description="unload an extension. use \"all\" to unload all extensions")
    async def extensions_unload(self, inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
        if extension == "all":
            successful_unloads = ""
            failed_unloads = ""
            for extension in self.bot.extensions:
                if extension.startswith("base"):
                    continue
                try:
                    self.bot.unload_extension(extension)
                    successful_unloads += f"unloaded {extension}\n"
                except Exception as e:
                    failed_unloads += f"failed to unload {extension}\n{e}\n"
            if successful_unloads != "":
                await inter.response.send_message(successful_unloads, ephemeral=True)
            if failed_unloads != "":
                await inter.response.send_message(failed_unloads, ephemeral=True)
            return
        try:
            self.bot.unload_extension(f"extensions.{extension}")
            await inter.response.send_message(f"unloaded {extension}", ephemeral=True)
        except Exception as e:
            await inter.response.send_message(f"failed to unload {extension}\n{e}", ephemeral=True)

    @manager.sub_command(name="reload", description="reload an extension. use \"all\" to reload all extensions")
    async def extensions_reload(self, inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
        if extension == "all":
            successful_reloads = ""
            failed_reloads = ""
            for extension in self.bot.extensions:
                if extension.startswith("base"):
                    continue
                try:
                    self.bot.reload_extension(extension)
                    successful_reloads += f"reloaded {extension}\n"
                except Exception as e:
                    failed_reloads += f"failed to reload {extension}\n{e}\n"
            if successful_reloads != "":
                await inter.response.send_message(successful_reloads, ephemeral=True)
            if failed_reloads != "":
                await inter.response.send_message(failed_reloads, ephemeral=True)
            return
        try:
            self.bot.reload_extension(f"extension.{extension}")
            await inter.response.send_message(f"reloaded {extension}", ephemeral=True)
        except Exception as e:
            await inter.response.send_message(f"failed to reload {extension}\n{e}", ephemeral=True)

    @manager.sub_command(name="list", description="list all currently running extensions")
    async def extensions_list(self, inter: disnake.ApplicationCommandInteraction) -> None:
        await inter.response.send_message(self.bot.extensions)


def setup(bot: commands.Bot):
    bot.add_cog(Manager(bot))
