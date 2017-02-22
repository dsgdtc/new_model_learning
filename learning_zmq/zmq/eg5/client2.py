#coding=utf-8  
'''
'''  
import zmq
import time
context = zmq.Context()  
client = context.socket(zmq.PUSH)  
client.connect('tcp://192.168.137.2:15000')  
count = 0
while True:
	count += 1  
	client.send('192.168.137.2: %d ' % count)  
	print '192.168.137.2',count
	time.sleep(0.001)
