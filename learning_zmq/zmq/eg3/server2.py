#coding=utf-8  
''' 
两个server一个client不行,client只识别一个server
send队列里只有2000默认只有个数
'''  
import zmq  
import time  
  
context = zmq.Context()  
server = context.socket(zmq.PUSH)  
#server.bind('ipc:///tmp/test.ipc')  
server.bind('tcp://127.0.0.1:15000')  
count = 0  
while True:  
	server.send("server2:%d" % count)  
	print ('send count: %d' % count)
	count +=1  
	time.sleep(0.1)
