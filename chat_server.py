import threading
import time
import logging
import grpc

from concurrent.futures import ThreadPoolExecutor
from chat_protobufs.chatroom_pb2_grpc import add_ChatServicer_to_server
from chat_protobufs.grpc_servicer import InfoService


logging.basicConfig(level=logging.INFO)
logging.getLogger("[CHAT SERVER]")


class ChatServer:

    def __init__(self, grpc_address):
        self._grpc_service = InfoService()
        self._grpc_address = grpc_address

    def _grpc_server(self) -> None:
        """ grpc service """
        grpc_server = grpc.server(ThreadPoolExecutor(max_workers=10))
        add_ChatServicer_to_server(self._grpc_service, grpc_server)
        grpc_server.add_insecure_port(self._grpc_address)
        logging.info(f"[CHAT SERVER]: Starting server on {self._grpc_address}")
        grpc_server.start()
        grpc_server.wait_for_termination()

    def _message_handler(self):
        last_message = 0
        while True:
            while len(self._grpc_service.message_handled) > last_message:
                logging.info(f"[CHAT SERVER]: Got message {self._grpc_service.message_handled[last_message]}")
                last_message += 1

    def _user_handler(self):
        last_user = 0
        while True:
            while len(self._grpc_service.connected_users) > last_user:
                logging.info(f"[CHAT SERVER]: Got user {self._grpc_service.connected_users[last_user]}")
                last_user += 1

    def run(self):
        """ Run Server """
        grpc_thread = threading.Thread(target=self._grpc_server)
        handler_thread = threading.Thread(target=self._message_handler)
        user_thread = threading.Thread(target=self._user_handler)
        handler_thread.start()
        time.sleep(5)
        grpc_thread.start()
        time.sleep(5)
        user_thread.start()
        grpc_thread.join()
        handler_thread.join()
        user_thread.join()
