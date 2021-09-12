#!/usr/bin/python
import getpass, telnetlib, time

class VsxTelnet:
    debugLevel = 0
    tn = None
    telnetHost = "192.168.20.208"
    telnetPort = 8102
    output = ""
    outList = []

    def __init__(self):
        self.tn = telnetlib.Telnet(None)
        self.tn.set_debuglevel(self.debugLevel)

    def command(self, cmd):
        self.openTelnet()
        self.outList = []
        self.output = self.tn.read_eager()
        self.outList.append(output)
        self.tn.write(cmd.encode('ascii') + "\r\n".encode('ascii'))
        time.sleep(0.5)
        done = False
        while not done:
            value = ""
            value = self.tn.read_eager()
            self.output += value
            if value == "":
                done = True

        self.outList.append(output)
        self.closeTelnet()

    def printLastCommandResult(self):
        print(self.outList)

    def openTelnet(self):
        self.tn.open(self.telnetHost, self.telnetPort)

    def closeTelnet(self):
        self.tn.close()


if __name__ == "__main__":
    v = VsxTelnet()
    #v.command("?V")
    v.command("095VL")
    v.printLastCommandResult()
    time.sleep(5)

    v.command("?V")
    v.printLastCommandResult()
    time.sleep(5)

    v.command("110VL")
    v.printLastCommandResult()
    time.sleep(5)

    v.command("095VL")
    v.printLastCommandResult()
    time.sleep(5)
