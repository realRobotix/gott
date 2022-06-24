import logging
import os
import disnake
import disnake.ext
from disnake.ext import commands
from dotenv import load_dotenv
import extensions


def setup_logging():
    logger = logging.getLogger('disnake')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename='disnake.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)


def main():
    print("running")
    bot.run(DISCORD_BOT_TOKEN)


bot = commands.Bot(command_prefix='!',
                   test_guilds=[970711821478686721], intents=disnake.Intents.all(), auto_sync=True, sync_commands=True)


@bot.slash_command(name="extensions", description="used to configure extensions")
async def extensions(inter: disnake.ApplicationCommandInteraction):
    if inter.author.id not in BOT_DEVELOPERS:
        await inter.response.send_message("only bot developers can use this command", ephemeral=True)
        return


@extensions.sub_command(name="load", description="load an extension. use \"all\" to load all extensions")
async def extensions_load(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if inter.author.id not in BOT_DEVELOPERS:
        await inter.response.send_message("only bot developers can use this command", ephemeral=True)
        return
    if extension == "all":
        for (dirpath, dirname, filenames) in os.walk("./extensions"):
            successful_loads = ""
            failed_loads = ""
            for file in filenames:
                fullPath = os.path.join(dirpath, file)
                if file.endswith(".py") and not file.startswith("_"):
                    extension = "extensions." + fullPath[:-
                                                         3].replace("/", ".").replace("\\", ".").split("extensions.")[1]
                    try:
                        bot.load_extension(extension)
                        successful_loads += f"loaded {extension}\n"
                    except Exception as e:
                        failed_loads += f"failed to load {extension}\n{e}\n"
            if successful_loads != "":
                await inter.response.send_message(successful_loads, ephemeral=True)
            if failed_loads != "":
                await inter.response.send_message(failed_loads, ephemeral=True)
        return
    try:
        bot.load_extension(f"extensions.{extension}")
        await inter.response.send_message(f"loaded {extension}", ephemeral=True)
    except Exception as e:
        await inter.response.send_message(f"failed to load {extension}\n{e}", ephemeral=True)


@extensions.sub_command(name="unload", description="unload an extension. use \"all\" to unload all extensions")
async def extensions_unload(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if inter.author.id not in BOT_DEVELOPERS:
        await inter.response.send_message("only bot developers can use this command", ephemeral=True)
        return
    if extension == "all":
        successful_unloads = ""
        failed_unloads = ""
        for extension in bot.extensions:
            try:
                bot.unload_extension(extension)
                successful_unloads += f"unloaded {extension}\n"
            except Exception as e:
                failed_unloads += f"failed to unload {extension}\n{e}\n"
        if successful_unloads != "":
            await inter.response.send_message(successful_unloads, ephemeral=True)
        if failed_unloads != "":
            await inter.response.send_message(failed_unloads, ephemeral=True)
        return
    try:
        bot.unload_extension(f"extensions.{extension}")
        await inter.response.send_message(f"unloaded {extension}", ephemeral=True)
    except Exception as e:
        await inter.response.send_message(f"failed to unload {extension}\n{e}", ephemeral=True)


@extensions.sub_command(name="reload", description="reload an extension. use \"all\" to reload all extensions")
async def extensions_reload(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if inter.author.id not in BOT_DEVELOPERS:
        await inter.response.send_message("you are not a bot developer")
        return
    if extension == "all":
        successful_reloads = ""
        failed_reloads = ""
        for extension in bot.extensions:
            try:
                bot.reload_extension(extension)
                successful_reloads += f"reloaded {extension}\n"
            except Exception as e:
                failed_reloads += f"failed to reload {extension}\n{e}\n"
        if successful_reloads != "":
            await inter.response.send_message(successful_reloads, ephemeral=True)
        if failed_reloads != "":
            await inter.response.send_message(failed_reloads, ephemeral=True)
        return
    try:
        bot.reload_extension(f"extension.{extension}")
        await inter.response.send_message(f"reloaded {extension}", ephemeral=True)
    except Exception as e:
        await inter.response.send_message(f"failed to reload {extension}\n{e}", ephemeral=True)


if __name__ == "__main__":
    try:
        try:
            load_dotenv()
        except Exception:
            pass
        try:
            DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']
            BOT_DEVELOPERS = list(
                map(int, os.environ['BOT_DEVELOPERS'].split('\n')))
        except Exception:
            print("missing environment variables")
            exit()
        setup_logging()
        main()
    except KeyboardInterrupt:
        print("shutting down")
