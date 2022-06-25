import logging
import os
import disnake
import disnake.ext
from disnake.ext import commands
from dotenv import load_dotenv
from utils.exeptions import *


def setup_logging():
    logger = logging.getLogger("disnake")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename="disnake.log", encoding="utf-8", mode="w")
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)


def main():
    print("running")
    for (dirpath, dirname, filenames) in os.walk("./extensions/base"):
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
                try:
                    bot.load_extension(extension)
                except Exception as e:
                    raise BaseLoadExeption("")
    bot.run(DISCORD_BOT_TOKEN)


bot = commands.Bot(
    command_prefix="!",
    test_guilds=[970711821478686721],
    intents=disnake.Intents.all(),
    auto_sync=True,
    sync_commands=True,
)


if __name__ == "__main__":
    try:
        try:
            load_dotenv()
        except Exception:
            pass
        try:
            DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
            BOT_DEVELOPERS = list(map(int, os.environ["BOT_DEVELOPERS"].split("\n")))
        except Exception:
            print("missing environment variables")
            exit()
        setup_logging()
        main()
    except KeyboardInterrupt:
        print("shutting down")
