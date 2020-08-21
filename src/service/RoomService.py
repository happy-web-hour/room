from src.repository.RoomRepository import RoomRepository


class RoomService:
    def __init__(self, repository: RoomRepository):
        self.__repository = repository

    def get_rooms(self, pin: str):
        return self.__repository.get_rooms(
            pin=pin
        )
    def get_all_rooms(self):
        return self.__repository.get_all_rooms()

    def add_user(self, room_id: str, user_id: str):
        self.__repository.add_user(
            room_id=room_id,
            user_id=user_id
        )
