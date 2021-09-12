#!/usr/bin/python
import getpass, telnetlib, time

# HOST = "192.168.20.208"
# PORT = 8102
#
# tn = telnetlib.Telnet(None)
# tn.set_debuglevel(5)
# tn.open(HOST, PORT)
# #out = tn.read_until("VOL".encode('ascii'), 20)
# out = tn.read_eager()
# tn.write("110VL".encode('ascii') + "\r\n".encode('ascii'))
# tn.close()
# print(out)

class VsxTelnet:
    debugLevel = 5
    tn = None
    telnetHost = "192.168.20.208"
    telnetPort = 8102
    output = ""

    def __init__(self):
        tn = telnetlib.Telnet(None)
        tn.set_debuglevel(self.debugLevel)

    def command(self, cmd):
        self.openTelnet()
        output = tn.read_eager()
        tn.write(cmd.encode('ascii') + "\r\n".encode('ascii'))
        time.sleep(0.5)
        done = False
        while not done:
            value = ""
            value = tn.read_eager()
            output += value
            if value == "":
                done = True

        self.closeTelnet()

    def printLastCommandResult(self):
        print(output)

    def openTelnet(self):
        tn.open(self.telnetHost, self.telnetHost)

    def closeTelnet(self):
        tn.close(self.telnetHost, self.telnetHost)


if __name__ == "__main__":
    v = VsxTelnet()
    v.command("?V")
    v.printLastCommandResult()
