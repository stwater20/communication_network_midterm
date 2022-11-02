import socket

local_ip = ""
local_port = 80
buffer_size = 1024

msg_from_server = "Hello UDP Client"
bytes_to_send = str.encode(msg_from_server)

UDP_server_socket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

UDP_server_socket.bind((local_ip, local_port))

print("UDP server up and listening")

while(True):
    bytes_address_pair = UDP_server_socket.recvfrom(buffer_size)
    message = bytes_address_pair[0]
    address = bytes_address_pair[1]

    client_msg = "Message from Client:{}".format(message)
    client_ip = "Client IP Address:{}".format(address)

    UDP_server_socket.sendto(bytes_to_send, address)