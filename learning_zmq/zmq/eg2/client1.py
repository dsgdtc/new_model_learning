#coding=utf-8  
''' 
'''  
import zmq  
import time
  
context = zmq.Context()  
print 'connect to hello world server'  
socket =  context.socket(zmq.REQ)  
socket.connect('tcp://localhost:5555')  
request = 0
#for request in range(1,10):  
while True:
	request += 1
	print 'send ',request,'...'  
	socket.send('client1')  
	try:
		message = socket.recv() 
		print 'received reply ',request,'[',message,']'
	except:
		print 'no message'
