import logging

from chat_protobufs.chatroom_pb2_grpc import ChatServicer
from chat_protobufs.chatroom_pb2 import Nothing, connectionConfirm, sendMessageRequest
from chat_protobufs.chatroom_pb2 import disconnectionConfirm, connectionRequest

logging.basicConfig(level=logging.INFO)


def pack_message(_message) -> sendMessageRequest:
    # Pack messages to be sent through gRPC channel
    return sendMessageRequest(
        sentMessage=_message['message'],
        userName=_message['user_name']
    )


def pack_user(_user) -> connectionRequest:
    # Pack gRPC message to send through channel
    return connectionRequest(
        userName=_user['user_name']
    )


class InfoService(ChatServicer):
    """
    Handles message requests
    Posts message back
    """

    def __init__(self):
        self.message_handled = []               # Contains all messages sent through server
        self.connected_users = []               # List of currently connected users
        self.disconnected_users = []            # List of users that disconnected

    def messageStream(self, request, context):
        if request.nothing is True:             # True for yielding all messages in server list
            last_message = 0
            while True:
                while len(self.message_handled) > last_message:
                    _message = self.message_handled[last_message]
                    last_message += 1
                    yield pack_message(_message)
        if request.nothing is False:            # False for yielding all connected users in server list
            last_user = 0
            while True:
                while len(self.connected_users) > last_user:
                    _user = self.connected_users[last_user]
                    last_user += 1
                    yield pack_user(_user)

    def sendMessage(self, request, context):
        _message = request.sentMessage
        _user_name = request.userName

        self.message_handled.append({   # Store sent message to server list
            'message': _message,
            'user_name': _user_name
        })

        logging.info(f"[INFO SERVICE]: Received message: {_message}")

        response = Nothing(nothing=True)    # Response is required so we just send a dummy Object
        return response

    def connectedUser(self, request, context):
        _new_user = request.userName
        if _new_user is not None:                       # Currently does not check for "username already exist"
            self.connected_users.append({
                'user_name': _new_user
            })
            return connectionConfirm(connected=True)    # User added to connected users list
        else:
            return connectionConfirm(connnected=False)  # No user was passed

    def onDisconnection(self, request, context):
        incoming = request.userName

        self.disconnected_users.append(incoming)
        self.connected_users = [item for item in self.connected_users if item['user_name'] != incoming]

        response = disconnectionConfirm(disconnected=True)
        return response
