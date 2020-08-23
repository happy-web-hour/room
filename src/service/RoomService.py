import uuid

from src.repository.ChatRepository import ChatRepository
from src.repository.RoomRepository import RoomRepository


class RoomService:
    def __init__(self, room_repository: RoomRepository, chat_repository: ChatRepository):
        self.__room_repository = room_repository
        self.__chat_repository = chat_repository
        self.__rooms_name = ["sala de jogos", "fumodromo", "fofoqueirxs", "rapaziada", "galera do fundao",
                             "tops", "soh devs", "frontenders", "backenders", "c level", "desce mais uma",
                             "los ousados"]

    def get_rooms(self, pin: str):
        return self.__room_repository.get_rooms(
            pin=pin
        )

    def create_room(self, pin: str):
        rooms = [
            {
                "roomId": str(uuid.uuid4()),
                "name": room_name,
                "users": []
            } for room_name in self.__rooms_name
        ]
        self.__room_repository.create_room({
            "pin": pin,
            "rooms": rooms
        })
        for room in rooms:
            self.__chat_repository.create_chat(
                room_id=room["roomId"]
            )

    def get_all_rooms(self):
        return self.__room_repository.get_all_rooms()

    def add_user(self, room_id: str, user_id: str):
        self.__room_repository.add_user(
            room_id=room_id,
            user_id=user_id
        )
        self.__chat_repository.add_user(
            room_id=room_id,
            user_id=user_id
        )

    def delete_user(self, room_id: str, user_id: str):
        self.__room_repository.delete_user(
            room_id=room_id,
            user_id=user_id
        )
        self.__chat_repository.delete_user(
            room_id=room_id,
            user_id=user_id
        )

    def delete_room(self, pin: str):
        self.__room_repository.delete_room(
            pin=pin
        )

    def list_users(self, room_id: str):
        return self.__room_repository.list_users(
            room_id=room_id
        )
