import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8220))

with open('output.txt', 'r') as csv_file:
    csv_reader = csv_file.readlines()
    for line in csv_reader:
        print('send to server: ',line)
        client_socket.send(line.encode('utf-8'))
        print("hey\n")
        #client_socket.send(line)
        while((client_socket.recv(2048).decode('utf-8')) != "ack"):
            print("waiting for ack")
        print("ack received!")
dmsg = "disconnect"
print("Disconnecting")
client_socket.send(dmsg.encode('utf-8'))

client_socket.close()
