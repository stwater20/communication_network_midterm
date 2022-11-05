import socket
import threading
import sys
buffer_size = 1024
#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
success = []
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(buffer_size)
            success.append(str(data.decode("utf-8")))
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            print(len(success))
            print(success)
            signal = False
            break

#Get host and port
host = input("Host: ")
port = int(input("Port: "))

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network
while True:
    message = input()
    sock.sendall(str.encode(message))
