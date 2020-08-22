import uuid

from src.repository.RoomRepository import RoomRepository


class RoomService:
    def __init__(self, repository: RoomRepository):
        self.__repository = repository
        self.__rooms_name = ["sala de jogos", "fumodromo", "fofoqueirxs", "rapaziada"]

    def get_rooms(self, pin: str):
        return self.__repository.get_rooms(
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
        self.__repository.create_room({
                "pin": pin,
                "rooms": rooms
            }
        )


    def get_all_rooms(self):
        return self.__repository.get_all_rooms()

    def add_user(self, room_id: str, user_id: str):
        self.__repository.add_user(
            room_id=room_id,
            user_id=user_id
        )

    def delete_user(self, room_id: str, user_id: str):
        self.__repository.delete_user(
            room_id=room_id,
            user_id=user_id
        )

    def delete_room(self, pin: str):
        self.__repository.delete_room(
            pin=pin
        )