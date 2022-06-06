import os
import disnake
import disnake.ext
from disnake.ext import commands
from config import DISCORD_BOT_TOKEN


def main():
    print("running")
    bot.run(DISCORD_BOT_TOKEN)


bot = commands.Bot(command_prefix='!',
                   test_guilds=[970711821478686721], intents=disnake.Intents.all(), auto_sync=True)


@bot.slash_command(name="extensions", description="used to configure extensions", channel_types=disnake.ChannelType.private, )
async def extensions(inter):
    pass


@extensions.sub_command(name="load", description="load an extension. use ```all``` to load all extensions")
async def extensions_load(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if extension == "all":
        for (dirpath, filenames) in os.walk("./extensions"):
            for file in filenames:
                fullPath = os.path.join(dirpath, file)
                if file.endswith(".py") and not file.startswith("_"):
                    extension = fullPath[:-
                                         3].replace("/", ".").replace("\\", ".")
                    try:
                        bot.load_extension(f"extensions.{extension}")
                        await inter.response.send_message(f"loaded {extension}")
                    except Exception as e:
                        await inter.response.send_message(f"failed to load {extension}\n{e}")
        return
    bot.load_extension(f"extensions.{extension}")
    await inter.response.send_message(f"loaded {extension}")


@extensions.sub_command(name="unload", description="unload an extension. use ```all``` to unload all extensions")
async def extensions_unload(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if extension == "all":
        for extension in bot.extensions:
            try:
                bot.unload_extension(extension)
                await inter.response.send_message(f"unloaded {extension}")
            except Exception as e:
                await inter.response.send_message(f"failed to unload {extension}\n{e}")
    bot.unload_extension(f"commands.{extension}")
    await inter.response.send_message(f"unloaded {extension}")


@extensions.sub_command(name="reload", description="reload an extension. use ```all``` to reload all extensions")
async def extensions_reload(inter: disnake.ApplicationCommandInteraction, extension: str) -> None:
    if extension == "all":
        for extension in bot.extensions:
            try:
                bot.reload_extension(extension)
                await inter.response.send_message(f"reloaded {extension}")
            except Exception as e:
                await inter.response.send_message(f"failed to reload {extension}\n{e}")
    bot.reload_extension(f"commands.{extension}")
    await inter.response.send_message(f"reloaded {extension}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("shutting down")
        exit(0)
    finally:
        bot.close()
