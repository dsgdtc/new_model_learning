#coding=utf-8  
''' 
'''  
import zmq  
import time  
  
context = zmq.Context()  
#server = context.socket(zmq.PUSH)  
server = context.socket(zmq.PULL)  
#server.bind('ipc:///tmp/test.ipc')  
server.connect('tcp://localhost:15000')  
count = 0  
while True:  
	server.send("server1:%d" % count)  
	print 'send','count'  
	count +=1  
	time.sleep(0.2)
