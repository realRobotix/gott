import os
from posixpath import dirname
import disnake
import disnake.ext
from disnake.ext import commands
import config


def main():
    print("running")
    bot.run(config.DISCORD_BOT_TOKEN)


bot = commands.Bot(command_prefix='!',
                   test_guilds=[970711821478686721], intents=disnake.Intents.all(), auto_sync=True)


@bot.slash_command(name="extensions", description="used to configure extensions")
async def extensions(inter: disnake.ApplicationCommandInteraction):
    if inter.author.id not in config.BOT_DEVELOPERS:
        await inter.response.send_message("only bot developers can use this command", ephemeral=True)
        return


@extensions.sub_command(name="load", description="load an extension. use ```all``` to load all extensions")
async def extensions_load(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if inter.author.id not in config.BOT_DEVELOPERS:
        await inter.response.send_message("only bot developers can use this command", ephemeral=True)
        return
    if extension == "all":
        for (dirpath, dirname, filenames) in os.walk("./extensions"):
            for file in filenames:
                fullPath = os.path.join(dirpath, file)
                if file.endswith(".py") and not file.startswith("_"):
                    extension = "extensions." + fullPath[:-
                                                         3].replace("/", ".").replace("\\", ".").split("extensions.")[1]
                    try:
                        bot.load_extension(extension)
                        await inter.response.send_message(f"loaded {extension}", ephemeral=True)
                    except Exception as e:
                        await inter.response.send_message(f"failed to load {extension}\n{e}", ephemeral=True)
        return
    try:
        bot.load_extension(f"extensions.{extension}")
        await inter.response.send_message(f"loaded {extension}", ephemeral=True)
    except Exception as e:
        await inter.response.send_message(f"failed to load {extension}\n{e}", ephemeral=True)


@extensions.sub_command(name="unload", description="unload an extension. use ```all``` to unload all extensions")
async def extensions_unload(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if inter.author.id not in config.BOT_DEVELOPERS:
        await inter.response.send_message("only bot developers can use this command", ephemeral=True)
        return
    if extension == "all":
        for extension in bot.extensions:
            try:
                bot.unload_extension(extension)
                await inter.response.send_message(f"unloaded {extension}", ephemeral=True)
            except Exception as e:
                await inter.response.send_message(f"failed to unload {extension}\n{e}", ephemeral=True)
        return
    try:
        bot.unload_extension(f"extensions.{extension}")
        await inter.response.send_message(f"unloaded {extension}", ephemeral=True)
    except Exception as e:
        await inter.response.send_message(f"failed to unload {extension}\n{e}", ephemeral=True)


@extensions.sub_command(name="reload", description="reload an extension. use ```all``` to reload all extensions")
async def extensions_reload(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if inter.author.id not in config.BOT_DEVELOPERS:
        await inter.response.send_message("you are not a bot developer")
        return
    if extension == "all":
        for extension in bot.extensions:
            try:
                bot.reload_extension(extension)
                await inter.response.send_message(f"reloaded {extension}", ephemeral=True)
            except Exception as e:
                await inter.response.send_message(f"failed to reload {extension}\n{e}", ephemeral=True)
        return
    try:
        bot.reload_extension(f"extension.{extension}")
        await inter.response.send_message(f"reloaded {extension}", ephemeral=True)
    except Exception as e:
        await inter.response.send_message(f"failed to reload {extension}\n{e}", ephemeral=True)
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("shutting down")
        exit(0)
    finally:
        bot.close()
