#/usr/bin/env python
#coding=utf-8  
''' 
订阅模式，如果设置了过滤条件，那么只会接收到以过滤条件开头的消息 
'''  
import sys  
import zmq  
import time  
IPC='ipc:///tmp/zmqeg1.ipc'
  
#  Socket to talk to server  
context = zmq.Context()  
socket = context.socket(zmq.SUB)  
  
print("Collecting updates from weather server...")  
#socket.connect("tcp://localhost:5556")  
socket.connect(IPC)  
  
# Subscribe to zipcode, default is NYC, 10001  
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10002"  
  
#此处设置过滤条件，只有以 zip_filter 开头的消息才会被接收  
socket.setsockopt(zmq.SUBSCRIBE, zip_filter)  
  
# Process 5 updates  
total_temp = 0  
for update_nbr in range(5):  
    print 'wait recv'  
    string = socket.recv()  
    print 'has recv'  
    time.sleep(1)  
    print string  
    zipcode, temperature, relhumidity = string.split()  
    total_temp += int(temperature)  
  
print("Average temperature for zipcode '%s' was %dF" % (  
      zip_filter, total_temp / update_nbr)  
)
