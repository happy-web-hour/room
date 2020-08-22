from flask import Blueprint, request
from flask_cors import cross_origin

from src.controller import service
from src.controller.UtilController import UtilController
from src.library.logger.Logger import Logger

chat_controller = Blueprint('ChatController', __name__)


class RoomController:
    @staticmethod
    @cross_origin()
    @chat_controller.route('/room/<string:pin>', methods=['GET'])
    def get_rooms(pin: str):
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"get_rooms: pin={pin}")
            response = service.get_rooms(
                pin=pin
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/room', methods=['GET'])
    def get_all_rooms():
        response: dict
        status_code: int = 200
        try:
            Logger.info(f"get_rooms:")
            response = service.get_all_rooms()
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/room/<string:room_id>/<string:user_id>', methods=['POST'])
    def add_user(room_id: str, user_id: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"add_user: room_id={room_id} user_id={user_id}")
            service.add_user(
                room_id=room_id,
                user_id=user_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/room/<string:room_id>/<string:user_id>', methods=['DELETE'])
    def delete_user(room_id: str, user_id: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"delete_user: room_id={room_id} user_id={user_id}")
            service.delete_user(
                room_id=room_id,
                user_id=user_id
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/room/<string:pin>', methods=['DELETE'])
    def delete_room(pin: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"delete_room: pin={pin}")
            service.delete_room(
                pin=pin
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)

    @staticmethod
    @cross_origin()
    @chat_controller.route('/room/<string:pin>', methods=['POST'])
    def create_room(pin: str):
        response: dict = {}
        status_code: int = 200
        try:
            Logger.info(f"create_room: pin={pin}")
            service.create_room(
                pin=pin
            )
        except Exception as exception:
            status_code = 500
            response = UtilController.build_error_payback(exception, status_code)

        return UtilController.build_response(response, status_code)
