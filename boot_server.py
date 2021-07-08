import logging
import argparse
import json

from chat_server import ChatServer

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='ChatRoom server')
    parser.add_argument('--connect', metavar='server_config_file',
                        type=str, required=True,
                        help='connect server to address')
    args = parser.parse_args()

    with open(args.connect, 'r') as f:
        config = json.loads(f.read())
        server = ChatServer(config['grpc_address'])
        server.run()

