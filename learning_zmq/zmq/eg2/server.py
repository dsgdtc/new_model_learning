#/usr/bin/env python
#coding=utf-8  
''' 
回复请求 
'''  
import zmq  
import time  
  
context = zmq.Context()  
socket = context.socket(zmq.XREP)  
socket.bind('tcp://*:5555')

#try:
#	socket.send('start')  
#except:
#	pass
while True:  
	message = socket.recv()  
	print 'received request: ' ,message  
	time.sleep(0.1)  
    #if message == 'client1':  
    #    socket.send('you are client1')  
    #else:  
    #    socket.send('you are client2')
	socket.send('lalala')
