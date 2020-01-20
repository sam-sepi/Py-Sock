
import socket
import sys

# SERVER IP
HOST = '127.0.0.1' 
# SERVER PORT
PORT = 60000

# WITH like TRY CATCH 
# ARGS IPv4 and TCP Prot.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    command = input(">> ")
    s.sendall(command.encode())
    data = s.recv(4096)
    print(str(data, "utf-8"))