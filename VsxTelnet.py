#!/usr/bin/python
import getpass
import telnetlib

HOST = "192.168.20.208"
PORT = 8102

tn = telnetlib.Telnet(None)
tn.open(HOST, PORT)
out = tn.read_until("VOL".encode('ascii'), 20)
tn.write("110VL".encode('ascii') + "\r\n".encode('ascii'))
print(out)
tn.close()
