import logging
import os
import disnake
import disnake.ext
from disnake.ext import commands
from utils.exeptions import *
from utils import db
from utils import env
import pathlib


class Gott(commands.Bot):
    def __init__(self):
        self.path = str(pathlib.Path(__file__).parent.resolve())
        self.env = env.Env()
        self.db = db.Mongo(self.path + self.env.DB_CERT_PATH)
        self.logger = logging.Logger("disnake", level=logging.DEBUG).addHandler(
            logging.FileHandler(
                filename=f"{self.path}/disnake.log", encoding="utf-8", mode="w"
            ).setFormatter(
                logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
            )
        )
        super().__init__(
            command_prefix="!",
            test_guilds=[970711821478686721, 691973470560452609],
            intents=disnake.Intents.all(),
            auto_sync=True,
            sync_commands=True,
            reload=self.env.BOT_AUTO_RELOAD,
        )
        for (dirpath, dirname, filenames) in os.walk(f"{self.path}/extensions/base"):
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
                        self.load_extension(extension)
                    except Exception as e:
                        raise ExtensionLoadExeption(f"Failed to load {extension}")
        if self.env.BOT_AUTO_LOAD:
            for (dirpath, dirname, filenames) in os.walk(f"{self.path}/extensions"):
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
                            self.load_extension(extension)
                        except Exception as e:
                            raise ExtensionLoadExeption(f"Failed to load {extension}")
        print("running")
        self.run(self.env.BOT_DISCORD_TOKEN)


if __name__ == "__main__":
    try:
        gott = Gott()
    except KeyboardInterrupt:
        print("shutting down")
