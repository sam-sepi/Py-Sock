# Socket error:

# 10061 Conn. Refused
# No connection could be made because the target computer actively refused it.

# 10035 Resource temporarily unavailable.
# This error is returned from operations on nonblocking sockets 
# that cannot be completed immediately, for example recv when 
# no data is queued to be read from the socket.

import socket

def scanner(address, port, delay):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Set a timeout on blocking socket operations
    s.settimeout(delay)
   
    try:
        ret = s.connect_ex((address, port))

        if ret == 0:
            print(str(port) + ' is Open')
            s.close()
        
        elif ret == 10061:
            print('Connection refused on port ' + str(port)) 
            s.close()
        
        elif ret == 10035:
            print('Resource temporarily unavailable on port ' + str(port))
            s.close()

    except Exception:
        pass

targets = [21, 22, 25, 80, 8080, 110, 143, 156, 194, 443]

for port in targets:
    scanner('hackthissite.org', port, 5)

"""
Resource temporarily unavailable on port 21
Connection refused on port 22
Resource temporarily unavailable on port 25
80 is Open
Resource temporarily unavailable on port 8080
Resource temporarily unavailable on port 110
Resource temporarily unavailable on port 143
Resource temporarily unavailable on port 156
Resource temporarily unavailable on port 194
443 is Open
"""