#coding=utf-8  
'''
'''  
import zmq  
context = zmq.Context()  
client = context.socket(zmq.PULL)  
client.connect('ipc:///tmp/test.ipc')  
  
while True:  
    msg = client.recv()  
    print msg
