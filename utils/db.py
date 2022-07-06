from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.codec_options import TypeRegistry


class Mongo(MongoClient):
    def __init__(self) -> None:
        self.uri = "mongodb+srv://discord-bot.jhhzwuy.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        super().__init__(
            host=self.uri,
            tz_aware=False,
            connect=True,
            type_registry=TypeRegistry(),
            tls=True,
            tlsCertificateKeyFile="C:/Users/Julian/Coding/gott/X509-cert-1874534277825620058.pem",
            server_api=ServerApi("1"),
        )


mongo = Mongo()
