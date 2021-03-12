from classes.trap import Trap
from classes import commands
from conf.strings import *

class PoLRModule(Trap):
    """wscript Command Trap"""

    def init(self):
        self.set_option('PROCESS', 'wscript.exe')
        self.set_option('DEBUGGER', ' ')

    def run(self):
        self.show_bat_info()