import os

import requests


class ChatRepository:
    def __init__(self):
        self.__host = os.getenv("CHAT_HOST")
        self.__port = os.getenv("CHAT_PORT")
        self.__chat_url = f"http://{self.__host}:{self.__port}"

    def create_chat(self, room_id: str):
        requests.post(
            url=f"{self.__chat_url}/chat/{room_id}"
        )

    def add_user(self, room_id: str, user_id: str):
        requests.patch(
            url=f"{self.__chat_url}/chat/{room_id}/{user_id}"
        )

    def delete_user(self, room_id: str, user_id: str):
        requests.delete(
            url=f"{self.__chat_url}/chat/{room_id}/{user_id}"
        )