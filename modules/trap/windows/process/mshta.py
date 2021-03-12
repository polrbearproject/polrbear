from classes.trap import Trap
from classes import commands
from conf.strings import *

class PoLRModule(Trap):
    """mshta Command Trap"""

    def init(self):
        self.set_option('PROCESS', 'mshta.exe')
        self.set_option('DEBUGGER', ' ')

    def run(self):
        self.show_bat_info()