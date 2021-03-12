from classes.trap import Trap
from classes import commands
from conf.strings import *

class PoLRModule(Trap):
    """hostname Command Trap"""

    def init(self):
        self.set_option('PROCESS', 'hostname.exe')
        self.set_option('DEBUGGER', 'none.exe')
        self.add_option('HOSTNAME', 'NSA-PC01', True, 'The fake hostname to be displayed')

    def output(self):
        msg = """%s""" % (
            self.get_option('HOSTNAME')
        )
        return str(msg)

    def code(self):
        # @ is required for a c# multiline string
        return str('@"' + self.output() + '"')

    def test(self):
        return str(self.output() + '\n')

    def createcmd(self):
        cmd = commands.PoLRCommand('hostname')        
        code = write_line % (self.code())
        cmd.code = code
        return cmd
    
    def showcode(self):
        print(self.createcmd().create_class())

    def run(self):        
        self.create_class(self.createcmd())


        
        
        