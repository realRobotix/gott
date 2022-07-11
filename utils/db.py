from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.codec_options import TypeRegistry
from utils import env


class Mongo(MongoClient):
    def __init__(self, cert: str) -> None:
        self.uri = "mongodb+srv://discord-bot.jhhzwuy.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        super().__init__(
            host=self.uri,
            tz_aware=False,
            connect=True,
            type_registry=TypeRegistry(),
            tls=True,
            tlsCertificateKeyFile=cert,
            server_api=ServerApi("1"),
        )
