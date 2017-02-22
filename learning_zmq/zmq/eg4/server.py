import zmq
import struct

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:5000")

while True:
    # receive the message
    msg = socket.recv()

    print "Message Size is: {0} [MB]".format( len(msg) / (1000 * 1000) )
