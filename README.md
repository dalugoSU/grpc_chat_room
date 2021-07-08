## gRPC Chat Room ##

Little project using gRPC's service to create a chatroom.
chat_protobufs folder contains services and messages used.
The server code file handles connection, checks and logging. A separate RPC file handles requests and responses.
gRPC handles the threads.

## Run The Code ##

```
Needs: grpcio and grpc-tools. 
```

## Boot Server ##
server is booted with a config file containing the server address and port
```
python boot_server.py --connect server_config.json
```

## Boot a Client ##
Boot clients with a config file containing the connection address and port. 
Client can be booted with an username. Otherwise it will start you as anonymous
```
No username: python boot_client.py --connect client_config.json
With username: python boot_client.py --user USERNAME --connect client_config.json
```

All set! Send messages accross each client :D
