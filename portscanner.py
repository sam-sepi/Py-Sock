# Socket error:

# 10061 Conn. Refused
# No connection could be made because the target computer actively refused it.

# 10035 Resource temporarily unavailable.
# This error is returned from operations on nonblocking sockets 
# that cannot be completed immediately, for example recv when 
# no data is queued to be read from the socket.

import socket
import time

# The concurrent.futures module provides a high-level interface 
# for asynchronously executing callables.

import concurrent.futures

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
        
        else:
            print('Errno ' + ret + ' on port ' + port) # print socket errno

    except Exception:
        pass

targets = [21, 22, 25, 80, 8080, 110, 143, 156, 194, 443]


# Execute
start_time = time.time()

NUM_WORKERS = 4
 
start_time = time.time()
 
with concurrent.futures.ThreadPoolExecutor(max_workers = NUM_WORKERS) as executor:
    futures = {executor.submit(scanner, 'mysitetest.org', port, 5) for port in targets}
    concurrent.futures.wait(futures)
 
end_time = time.time()

print("Time execution: %s secs" % (end_time - start_time))

"""
21 is Open
80 is Open
Connection refused on port 110
Connection refused on port 8080
Connection refused on port 156
Connection refused on port 143
443 is Open
Connection refused on port 194
Resource temporarily unavailable on port 25
Resource temporarily unavailable on port 22
Time execution: 5.011286735534668 secs

"""