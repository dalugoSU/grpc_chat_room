import logging
import argparse
import json
import grpc

from client_side import ClientSide
from chat_protobufs.chatroom_pb2_grpc import ChatStub


def run_client(server_address, name):
    if name == 'None':
        name = 'Anonymous'
    with grpc.insecure_channel(server_address) as channel:
        stub = ChatStub(channel)
        client_stub = ClientSide(stub, user_name=name)
        client_stub.run()



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='ChatRoom server')
    parser.add_argument('--user', metavar='name of user connecting',
                        type=str, required=False,
                        help='Name of user on client side')
    parser.add_argument('--connect', metavar='server_config_file',
                        type=str, required=True,
                        help='connect server to address')
    args = parser.parse_args()

    with open(args.connect, 'r') as f:
        config = json.loads(f.read())
        run_client(server_address=config['server_address'],
                   name=str(args.user).strip("'"))
