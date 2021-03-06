from classes.trap import Trap
from classes import commands
from conf.strings import *

class PoLRModule(Trap):
    """wmic Command Trap"""

    def init(self):
        self.set_option('PROCESS', 'wmic.exe')
        self.set_option('DEBUGGER', ' ')

    def run(self):
        self.show_bat_info()