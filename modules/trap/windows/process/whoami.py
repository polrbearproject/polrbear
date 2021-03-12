from classes.trap import Trap
from classes import commands
from conf.strings import *

class PoLRModule(Trap):
    """whoami Command Trap"""

    def init(self):
        self.set_option('PROCESS', 'whoami.exe')
        self.set_option('DEBUGGER', 'none.exe')
        self.add_option('DOMAIN', 'nsa', True, 'The fake domain name to be displayed')
        self.add_option('USERNAME', 'agent.smith', True, 'The fake username to be displayed')

    def output(self):
        msg = """%s\%s""" % (
            self.get_option('DOMAIN'), 
            self.get_option('USERNAME')
        )
        return str(msg)

    def code(self):
        # @ is required for a c# multiline string
        return str('@"' + self.output() + '"')

    def test(self):
        return str(self.output() + '\n')

    def createcmd(self):
        cmd = commands.PoLRCommand('whoami')        
        code = write_line % (self.code())
        cmd.code = code
        return cmd
    
    def showcode(self):
        print(self.createcmd().create_class())

    def run(self):        
        self.create_class(self.createcmd())


        
        
        