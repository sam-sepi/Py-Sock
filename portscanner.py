
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
            print(str(port) + ' is Filtered')
            s.close()
        
        else:
            print(str(port) + ' is Closed')
            s.close()

    except Exception:
        pass

targets = [21, 22, 25, 80, 8080, 110, 143, 156, 194, 443]

for port in targets:
    scanner('hackthissite.org', port, 5)

"""
21 is Closed
22 is Filtered
25 is Closed
80 is Open
8080 is Closed
110 is Closed
143 is Closed
156 is Closed
194 is Closed
443 is Open
"""