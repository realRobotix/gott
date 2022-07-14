from dotenv import load_dotenv
import os


class Env:
    def __init__(self) -> None:
        try:
            load_dotenv()
        except Exception:
            pass
        self.BOT_DISCORD_TOKEN: str = os.environ["BOT_DISCORD_TOKEN"]
        self.BOT_DEVELOPERS: list = list(
            map(int, os.environ["BOT_DEVELOPERS"].split("\n"))
        )
        self.BOT_AUTO_RELOAD: bool = os.environ["BOT_AUTO_RELOAD"]
        self.BOT_AUTO_LOAD: bool = os.environ["BOT_AUTO_LOAD"]
        self.DB_CERT_PATH: str = os.environ["DB_CERT_PATH"]
        self.THEDOGAPI_API_KEY: str = os.environ["THEDOGAPI_API_KEY"]
        self.THECATAPI_API_KEY: str = os.environ["THECATAPI_API_KEY"]
