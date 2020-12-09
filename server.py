import os
import sys
import threading
import select
import socket
import getpass
import base64
from cryptography.fernet import Fernet

#Acquire the key from the file generated by keygen.py
file = open('keyFile.key', 'rb')
key = file.read()
file.close()
#print(key)

#Check if all arguments are inputted
if len(sys.argv) != 3:
    print("Please input arguments: python script, IP, Port")
    exit()

#Extract IP and port from arguments
host_ip = str(sys.argv[1])
host_port = int(sys.argv[2])

#Create and setup socket connection
host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host.bind((host_ip, host_port))

#Username for chat room
username = raw_input("Enter username: ")

host.listen(1)
print("Listening for connection...")

client, address = host.accept()
print(address[0] + " has connected")

#Recieve username of client
clientName = (client.recv(1024)).decode()
print(clientName + " has entered the chat")

#Send host username
client.send(username.encode())

while True:
    #Input message as string format
    sendMsg = raw_input("Me (Enter 'quit' to close chat): ")
    
    #Exit chat condition
    #Messages are first encoded then encrypted using the 
    #cryptography package. The f variable is the key obtained
    #from the keygen.py script.
    if sendMsg.lower() == "quit":
        encodeMsg = sendMsg.encode()
        f = Fernet(key)
        encryptedMsg = f.encrypt(encodeMsg)
        client.send(encryptedMsg)
        client.close()
        print("Chat has ended")
        exit()
    else:
        encodeMsg = sendMsg.encode()
        f = Fernet(key)
        encryptedMsg = f.encrypt(encodeMsg)
        client.send(encryptedMsg)

    #Decrypt then decode messages using cryptography package
    recvEncryptMsg = client.recv(1024)
    decryptedMsg = f.decrypt(recvEncryptMsg)
    recvMsg = decryptedMsg.decode()
    print(clientName + ": " + recvMsg)
    if recvMsg.lower() == "quit":
        client.close()
        print("Chat has ended")
        exit()