## gRPC Chat Room ##

Little project using gRPC's service to create a chatroom.
chat_protobufs folder contains services and messages used.
The server code file handles connection, checks and logging. A separate RPC file handles requests and responses.
gRPC handles the threads.

## What it looks Like ##
'''
![Alt text](examples/chat_example.JPG?raw=true "Example chat and logs")
'''

## What you Need ##
Needs: grpcio and grpc-tools
```
pip install -r requirements.txt
```

## Client Config ##
client_config.json needs to be updated with the server IP
if you want to connect over LAN, change it to your wireless connection's IPv4 number for clients on your network; or use server IP.
If you want to try it out in your own machine, change to:
```
127.0.0.1:50052
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
