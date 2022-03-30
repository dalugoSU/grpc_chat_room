from grpc_tools import protoc

"""
Proto command to generate your files.
Whenever a change is made in your .proto file, run this file in this directory.
i.e 
    cd chat_protobufs
    python3 proto_gen.py
"""


def regen_proto_file():
    protoc.main((
        'python -m',
        '--python_out=.',
        '--grpc_python_out=.',
        '--experimental_allow_proto3_optional',
        'chatroom.proto'  # Change this to your proto file target
    ))


if __name__ == "__main__":
    regen_proto_file()
