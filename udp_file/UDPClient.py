import socket

buffer_size = 1024

host = input("Host: ")
port = int(input("Port: "))
server_address_port = (host, port)



count = 0
success = []
with open(r'./udp_file/client/file.txt', 'r', encoding = 'utf-8') as file:
    new_line = file.readline()
    while new_line is not None and new_line != '':
        try:
            UDP_client_socket = socket.socket(family= socket.AF_INET, type = socket.SOCK_DGRAM)
            msg_from_client = "{} {}".format(count, new_line)
            bytes_to_send = str.encode(msg_from_client)
            UDP_client_socket.sendto(bytes_to_send, server_address_port)
            # msg_from_server = UDP_client_socket.recvfrom(buffer_size)
            # success.append(msg_from_server[0])
            UDP_client_socket.close()
        except Exception as e:
            print(str(e))
        new_line = file.readline()
        print(count)
        count += 1
print(success)