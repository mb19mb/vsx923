#!/usr/bin/python
import getpass
import telnetlib

HOST = "192.168.20.208"
PORT = 8102

tn = telnetlib.Telnet(None)
tn.set_debuglevel(5)
tn.open(HOST, PORT)
out = tn.read_until("VOL".encode('ascii'), 20)
#out = tn.read_all()
tn.write("110VL".encode('ascii') + "\r\n".encode('ascii'))
tn.close()
print(out)
