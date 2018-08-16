#!usr/bin/env/ python

import socket

host = raw_input("Enter URL to Test:")

port = int(raw_input("Enter Port Number:"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

client.send("GET / HTTP/1.1\r\nHost:" + host + "\r\n\r\n")

resp = client.recv(4096)

print resp

