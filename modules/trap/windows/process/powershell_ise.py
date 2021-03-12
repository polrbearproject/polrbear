from classes.trap import Trap
from classes import commands
from conf.strings import *

class PoLRModule(Trap):
    """powershell_ise Command Trap"""

    def init(self):
        self.set_option('PROCESS', 'powershell_ise.exe')
        self.set_option('DEBUGGER', ' ')

    def run(self):
        self.show_bat_info()