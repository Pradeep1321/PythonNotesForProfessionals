"""
Chapter 121: Sockets
Parameter                   Description
socket.AF_UNIX          UNIX Socket
socket.AF_INET          IPv4
socket.AF_INET6         IPv6
socket.SOCK_STREAM      TCP
socket.SOCK_DGRAM       UDP

Section 121.1: Raw Sockets on Linux
First you disable your network card's automatic checksumming:
sudo ethtool -K eth1 tx off

Then send your packet, using a SOCK_RAW socket:
#!/usr/bin/env python
from socket import socket, AF_PACKET, SOCK_RAW
s = socket(AF_PACKET, SOCK_RAW)
s.bind(("eth1", 0))
# We're putting together an ethernet frame here,
# but you could have anything you want instead
# Have a look at the 'struct' module for more
# flexible packing/unpacking of binary data
# and 'binascii' for 32 bit CRC
src_addr = "\x01\x02\x03\x04\x05\x06"
dst_addr = "\x01\x02\x03\x04\x05\x06"
payload = ("["*30)+"PAYLOAD"+("]"*30)
checksum = "\x1a\x2b\x3c\x4d"
ethertype = "\x08\x01"
s.send(dst_addr+src_addr+ethertype+payload+checksum)

Section 121.2: Sending data via UDP
UDP is a connectionless protocol. Messages to other processes or computers are sent without establishing any sort
of connection. There is no automatic confirmation if your message has been received. UDP is usually used in
latency sensitive applications or in applications sending network wide broadcasts

from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
msg = ("Hello you there!").encode('utf-8') # socket.sendto() takes bytes as input, hence we must
encode the string first.
s.sendto(msg, ('localhost', 6667))

Section 121.3: Receiving data via UDP
socket.recvfromthus returns a tuple (msg [the message the socket received],addr [the address of the sender])
A UDP server using solely the socket module:

from socket import socket, AF_INET, SOCK_DGRAM

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('localhost', 6667))
while True:
    msg, addr = sock.recvfrom(8192) # This is the amount of bytes to read at maximum
    print("Got message from %s: %s" % (addr, msg))

Below is an alternative implementation using socketserver.UDPServer:

from socketserver import BaseRequestHandler, UDPServer
class MyHandler(BaseRequestHandler):
    def handle(self):
        print("Got connection from: %s" % self.client_address)
        msg, sock = self.request
        print("It said: %s" % msg)
        sock.sendto("Got your message!".encode(), self.client_address) # Send reply

serv = UDPServer(('localhost', 6667), MyHandler)
serv.serve_forever()
By default, sockets block. This means that execution of the script will wait until the socket receives data.

Section 121.4: Sending data via TCP
from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 6667)) # The address of the TCP server listening
s.send(b'Hello')
s.close()

Section 121.5: Multi-threaded TCP Socket Server
When run with no arguments, this program starts a TCP socket server that listens for connections to 127.0.0.1 on
port 5000. The server handles each connection in a separate thread
When run with the -c argument, this program connects to the server, reads the client list, and prints it out. The
client list is transferred as a JSON string. The client name may be specified by passing the -n argument. By passing
different names, the effect on the client list may be observed.


Chapter 122: Websockets
Section 122.1: Simple Echo with aiohttp
aiohttp provides asynchronous websockets

Python 3.x Version ≥ 3.5
import asyncio
from aiohttp import ClientSession
with ClientSession() as session:
    async def hello_world():
        websocket = await session.ws_connect("wss://echo.websocket.org")
        websocket.send_str("Hello, world!")
        print("Received:", (await websocket.receive()).data)
        await websocket.close()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello_world())

Section 122.2: Wrapper Class with aiohttp
aiohttp.ClientSession may be used as a parent for a custom WebSocket class.

Python 3.x Version ≥ 3.5
import asyncio
from aiohttp import ClientSession

class EchoWebSocket(ClientSession):
    URL = "wss://echo.websocket.org"
    def __init__(self):
        super().__init__()
        self.websocket = None
    async def connect(self):
        ""Connect to the WebSocket.""
        self.websocket = await self.ws_connect(self.URL)
    async def send(self, message):
        ""Send a message to the WebSocket.""
        assert self.websocket is not None, "You must connect first!"
        self.websocket.send_str(message)
        print("Sent:", message)
    async def receive(self):
        ..........

Section 122.3: Using Autobahn as a Websocket Factory
The Autobahn package can be used for Python web socket server factories.
To install, typically one would simply use the terminal command
(For Linux):
sudo pip install autobahn
(For Windows):
python -m pip install autobahn

Chapter 123: Sockets And Message Encryption/Decryption Between Client and Server
Cryptography is used for security purposes. There are not so many examples of Encryption/Decryption in Python
using IDEA encryption MODE CTR. Aim of this documentation :
Extend and implement of the RSA Digital Signature scheme in station-to-station communication. Using Hashing for
integrity of message, that is SHA-1. Produce simple Key Transport protocol. Encrypt Key with IDEA encryption. Mode
of Block Cipher is Counter Mode

Section 123.1: Server side Implementation


"""

#client_list.py
import argparse
import json
import socket
import threading

def handle_client(client_list, conn, address):
    name = conn.recv(1024)
    entry = dict(zip(['name', 'address', 'port'], [name, address[0], address[1]]))
    client_list[name] = entry
    conn.sendall(json.dumps(client_list))
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

def server(client_list):
    print("Starting server...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 5000))
    s.listen(5)
    while True:
        (conn, address) = s.accept()
        t = threading.Thread(target=handle_client, args=(client_list, conn, address))
        t.daemon = True
        t.start()
def client(name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 5000))
    s.send(name)
    data = s.recv(1024)
    result = json.loads(data)
    print(json.dumps(result, indent=4))

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', dest='client', action='store_true')
    parser.add_argument('-n', dest='name', type=str, default='name')
    result = parser.parse_args()
    return result

def main():
    client_list = dict()
    args = parse_arguments()
    if args.client:
        client(args.name)
    else:
        try:
            server(client_list)
        except KeyboardInterrupt:
            print("Keyboard interrupt")
if __name__ == '__main__':
    main()


#Client Output
