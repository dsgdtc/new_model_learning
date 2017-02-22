#coding=utf-8  
''' 
服务端，发布模式 
'''  
import zmq  
import time  
from random import randrange  
IPC='ipc:///tmp/zmqeg1.ipc'
      
context = zmq.Context()  
socket = context.socket(zmq.PUB)  
socket.bind(IPC)  
      
while True:  
#    zipcode = randrange(1, 100000)  
    temperature = randrange(-80, 135)  
    relhumidity = randrange(10, 60)  
      
    socket.send("%i %i %i" % (10002,temperature , relhumidity))  
