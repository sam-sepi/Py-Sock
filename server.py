import socket
import subprocess

# localhost
HOST = '127.0.0.1'
# port > 1023
PORT = 60000

# AF_INET -> IPv4
# SOCK_STREAM -> TCP

# With -> This allows common try…except…finally 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    # with
    with conn:
        print('Connected by', addr)
        # Infin. Loop
        while True:
            req = conn.recv(4096) # request command
            if not req:
                break # no data end loop
            resp = subprocess.run(req.decode(), stdout = subprocess.PIPE, stderr = subprocess.PIPE) # run subprocess
            data = resp.stdout + resp.stderr
            conn.sendall(data) # send resp