#coding=utf-8  
'''
'''  
import zmq  
import time
context = zmq.Context()  
client = context.socket(zmq.PULL)  
client.connect('ipc:///tmp/test.ipc')  
 

while True:  
	while True:
		try:
			msg = client.recv(zmq.NOBLOCK)  
		except:
			break
		print msg
		time.sleep(0.05)
