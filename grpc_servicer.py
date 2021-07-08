import logging
from chat_protobufs.chatroom_pb2_grpc import ChatServicer
from chat_protobufs.chatroom_pb2 import Nothing, connectionConfirm, sendMessageRequest

logging.basicConfig(level=logging.INFO)


def pack_message(_message):
    # Pack messages
    return sendMessageRequest(
        sentMessage=_message['message'],
        userName=_message['user_name']
    )


class InfoService(ChatServicer):
    """
    Handles message requests
    Posts message back
    """
    def __init__(self):
        self.message_handled = []
        self.connected_users = []

    def messageStream(self, request, context):
        last_message = 0
        while True:
            while len(self.message_handled) > last_message:
                _message = self.message_handled[last_message]
                last_message += 1
                yield pack_message(_message)

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
        user = request.userName
        if user is not None:
            self.connected_users.append(user)
            return connectionConfirm(connected=True)
        else:
            return connectionConfirm(connnected=False)

