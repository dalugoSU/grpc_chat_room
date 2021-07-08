from grpc_tools import protoc

protoc.main((
    'python -m',
    '--python_out=.',
    '--grpc_python_out=.',
    '--experimental_allow_proto3_optional',
    'chatroom.proto'
))