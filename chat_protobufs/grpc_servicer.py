import logging
from chat_protobufs.chatroom_pb2_grpc import ChatServicer
from chat_protobufs.chatroom_pb2 import Nothing, connectionConfirm, sendMessageRequest, disconnectionConfirm, \
    connectionRequest

logging.basicConfig(level=logging.INFO)


def pack_message(_message):
    # Pack messages
    return sendMessageRequest(
        sentMessage=_message['message'],
        userName=_message['user_name']
    )


def pack_user(_user):
    return connectionRequest(
        userName=_user['user_name']
    )


class InfoService(ChatServicer):
    """
    Handles message requests
    Posts message back
    """

    def __init__(self):
        self.message_handled = []
        self.connected_users = []
        self.disconnected_users = []

    def messageStream(self, request, context):
        if request.nothing is True:
            last_message = 0
            while True:
                while len(self.message_handled) > last_message:
                    _message = self.message_handled[last_message]
                    last_message += 1
                    yield pack_message(_message)
        if request.nothing is False:
            last_user = 0
            while True:
                while len(self.connected_users) > last_user:
                    _user = self.connected_users[last_user]
                    last_user += 1
                    yield pack_user(_user)

    def sendMessage(self, request, context):
        _message = request.sentMessage
        _user_name = request.userName
        self.message_handled.append({
            'message': _message,
            'user_name': _user_name
        })
        logging.info(f"[INFO SERVICE]: Received message: {_message}")
        response = Nothing(nothing=True)
        return response

    def connectedUser(self, request, context):
        _new_user = request.userName
        if _new_user is not None:
            self.connected_users.append({
                'user_name': _new_user
            })
            return connectionConfirm(connected=True)
        else:
            return connectionConfirm(connnected=False)

    def onDisconnection(self, request, context):
        incoming = request.userName
        self.disconnected_users.append(incoming)
        self.connected_users = [item for item in self.connected_users if item['user_name'] != incoming]
        response = disconnectionConfirm(disconnected=True)
        return response
