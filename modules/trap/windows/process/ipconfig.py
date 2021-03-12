from classes.trap import Trap
from classes import commands
from conf.strings import *

class PoLRModule(Trap):
    """ipconfig Command Trap"""

    def init(self):
        self.set_option('PROCESS', 'ipconfig.exe')
        self.set_option('DEBUGGER', 'none.exe')
        self.add_option('IPADDRESS', '10.10.150.5', True, 'The fake IP address to be displayed')
        self.add_option('SUBNET', '255.255.0.0', True, 'The fake subnet to be displayed')
        self.add_option('GATEWAY', '10.10.1.1', True, 'The fake gateway to be displayed')

    def output(self):
        msg = """
Windows IP Configuration


Ethernet adapter Ethernet:
   Connection -specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : %s
   Subnet Mask . . . . . . . . . . . : %s
   Default Gateway . . . . . . . . . : %s""" % (
            self.get_option('IPADDRESS'), 
            self.get_option('SUBNET'), 
            self.get_option('GATEWAY')
        )
        return str(msg)

    def code(self):
        # @ is required for a c# multiline string
        return str('@"' + self.output() + '"')

    def test(self):
        return str(self.output() + '\n')

    def createcmd(self):
        cmd = commands.PoLRCommand('ipconfig')        
        code = write_line % (self.code())
        cmd.code = code
        return cmd
    
    def showcode(self):
        print(self.createcmd().create_class())

    def run(self):        
        self.create_class(self.createcmd())
        