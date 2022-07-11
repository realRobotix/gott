import logging
import os
import disnake
import disnake.ext
from disnake.ext import commands
from utils.exeptions import *
from utils import db
from utils import env


class Gott(commands.Bot):
    def __init__(self):
        self.env = env.Env()
        self.db = db.Mongo(self.env.DB_CERT_PATH)
        super().__init__(
            command_prefix="!",
            test_guilds=[970711821478686721, 691973470560452609],
            intents=disnake.Intents.all(),
            auto_sync=True,
            sync_commands=True,
            reload=True,
        )


def setup_logging():
    logger = logging.getLogger("disnake")
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename="disnake.log", encoding="utf-8", mode="w")
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)


def main():
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
                    Gott.load_extension(extension)
                except Exception as e:
                    raise BaseLoadExeption("")
    print("running")
    Gott.run(env.DISCORD_BOT_TOKEN)


if __name__ == "__main__":
    try:
        setup_logging()
        main()
    except KeyboardInterrupt:
        print("shutting down")
