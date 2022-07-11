from dotenv import load_dotenv
import os


class Env:
    def __init__(self) -> None:
        try:
            load_dotenv()
        except Exception:
            pass
        self.DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
        self.BOT_DEVELOPERS = list(map(int, os.environ["BOT_DEVELOPERS"].split("\n")))
        self.DB_CERT_PATH = os.environ["DB_CERT_PATH"]
        self.THEDOGAPI_API_KEY = os.environ["THEDOGAPI_API_KEY"]
        self.THECATAPI_API_KEY = os.environ["THECATAPI_API_KEY"]
