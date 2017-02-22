import zmq
import struct
import time

# define a string of size 4[MB] 
msgToSend = struct.pack('i', 45) * 1000 * 1000 

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://127.0.0.1:5000")

# print the message size in bytes
count=0
while True:
	count += 1
	print len(msgToSend)
	socket.send(msgToSend)
	socket.send('%d' % count)
	time.sleep(0.01)	
