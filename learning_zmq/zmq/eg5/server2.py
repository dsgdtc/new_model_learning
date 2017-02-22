#coding=utf-8  
''' 
两个server一个client不行,client只识别一个server
send队列里只有2000默认只有个数
'''  
import zmq  
import time  
  
context = zmq.Context()  
server = context.socket(zmq.PULL)  
#server.bind('ipc:///tmp/test.ipc')  
server.bind('tcp://*:15000')  
while True:  
	msg = server.recv()  
	print ('%s' % msg)
	time.sleep(0.01)
