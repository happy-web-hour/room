import os

from src.library.database.Mongo import Mongo


class RoomRepository:
    def __init__(self):
        self.__mongo: Mongo = Mongo(
            host=os.getenv("MONGO_HOST"),
            port=int(os.getenv("MONGO_PORT")),
            default_db=os.getenv("MONGO_INITDB_DATABASE")
        )
        self.__room = os.getenv("MONGO_ROOM_DB")

    def get_rooms(self, pin: str):
        arr = self.__mongo.find_by(
            collection=self.__room,
            query={
                "pin": pin
            }
        )
        return arr["rooms"]

    def add_user(self, room_id: str, user_id: str):
        self.__mongo.update_element(
            collection=self.__room,
            query={
                "rooms": {
                    "$elemMatch": {
                        "roomId": room_id
                    }
                }
            },
            obj=[{"$set": {"rooms": {"users": {"$concatArrays": ["$users", [user_id]]}}}}]
        )

    def get_all_rooms(self):
        return [elem for elem in self.__mongo.find_all(self.__room)]
