from src.repository.RoomRepository import RoomRepository
from src.service.RoomService import RoomService

repository = RoomRepository()

service = RoomService(
    repository=repository
)
