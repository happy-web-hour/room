from src.repository.ChatRepository import ChatRepository
from src.repository.RoomRepository import RoomRepository
from src.service.RoomService import RoomService

service = RoomService(
    room_repository=RoomRepository(),
    chat_repository=ChatRepository()
)
