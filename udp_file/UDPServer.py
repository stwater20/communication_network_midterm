import socket

local_ip = "192.168.0.11"
local_port = 614
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
    client_msg = "{}".format(message)
    client_ip = "Client IP Address:{}".format(address)
    rec_content = client_msg.split()
    rec_num = rec_content[0]
    rec_str = rec_content[1]
    print(rec_num)
    with open('./udp_file/server/file.txt', 'a', encoding = 'utf-8') as of:
        of.write(rec_str + '\n')
    bytes_to_send = str.encode(rec_num)
    # UDP_server_socket.sendto(bytes_to_send, address)

   