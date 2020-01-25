
import socket

def scanner(address, port, delay):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(delay)
   
    try:
        ret = s.connect_ex((address, port))

        if ret == 0:
            print(str(port) + ' is Open')
            s.close()
        
        else:
            print(str(port) + ' is Filtered')
            s.close()

    except Exception:
        pass


targets = [21, 22, 25, 80, 8080, 110, 143, 156, 194, 443]


for port in targets:
    scanner('hackthissite.org', port, 1)

"""
21 is Filtered
22 is Filtered
25 is Filtered
80 is Open
8080 is Filtered
110 is Filtered
143 is Filtered
156 is Filtered
194 is Filtered
443 is Open
"""