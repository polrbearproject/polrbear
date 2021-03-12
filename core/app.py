#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import importlib, os, platform, subprocess, shutil
from conf import strings
from util import path
from conf.strings import *

modfiles = []

def showmodules():
    global modfiles
    modidx = 0
    modfiles = path.getmodules('.')
    print(show_mod)
    print(shmod_header)
    print(shmod_hdrsep)                    
    for mf in modfiles:
        modidx += 1
        print(shmod_line % (modidx, mf))
    print('')

def main():
    global modfiles
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

    print(logo)
    print(version_line)
        
    module = None
    cmds = path.getcommands('.')
    if len(cmds) > 0:
        print(status_info % ('There are command files from a previous session.'))
        for cmd in cmds:
            print(status_info % (status_detail % ('-- ' + cmd)))
        print(status_info % 'Use the %s command to remove them.' % (bcolors.WHITE + 'clean' + bcolors.END)) or 'Y'

    while 1:
        try:
            resp = prompt()
        except EOFError:
            resp = 'quit'
            print('')

        if resp is not None:            
            if resp == 'quit' or resp == 'exit':
                exit(0)
            elif resp == 'clean':
                rsp = input("This will remove all of the command files. Are you sure? %s (default %s): " % ((bcolors.BOLD + bcolors.GREEN + 'Y' + bcolors.END + 'es/' + bcolors.BOLD + bcolors.RED + 'N' + bcolors.END + 'o'), (bcolors.BOLD + bcolors.RED + 'N' + bcolors.END)))
                if rsp.upper() == 'Y':
                    shutil.rmtree('./mono/none/Commands', ignore_errors=True)
                    os.mkdir('./mono/none/Commands')
                    if os.path.isfile('./polrbear.bat'):
                        os.remove('./polrbear.bat')
                    print(status_info % 'Removed all previous command files.')
            elif resp == 'build':
                cmds = path.getcommands('.')
                if len(cmds) > 0:
                    shutil.rmtree('./mono/none/bin', ignore_errors=True)
                    shutil.rmtree('./mono/none/obj', ignore_errors=True)
                    for cmd in cmds:
                        print(status_info % ('Added command %s' % (status_detail % cmd)))
                    print(status_info % 'Building solution, please wait...')
                    print('=' * 17 + (status_title % '[msbuild output]') + '=' * 17)
                    if platform.system() == 'Linux':
                        subprocess.run(['msbuild', './mono/none/none.sln'])
                    else:
                        subprocess.run(['c:/windows/Microsoft.NET/Framework/v4.0.30319/msbuild.exe', './mono/none/none.sln'])                    
                    print('=' * 50)
                    print(status_okay % 'Successfully created %s' % (status_detail % 'none.exe'))
                else:
                    print(status_warn % 'There are no commands defined. Select a module with the \'use\' command and type \'run\' to add a command.')
            elif resp == 'back':
                strings.mod_type = ''
                strings.mod_name = ''
                module = None
            elif resp == 'run' and module is not None:
                module.run()
            elif resp[:3] == 'set' and module is not None:
                keyval = resp[4:]
                sep = keyval.find(' ')
                if sep > -1 :
                    key = resp[4:4 + sep]                
                    if module.is_option(key):
                        val = resp[4 + sep + 1:]
                        module.set_option(key, val)
                        print("set %s => %s" % (key, val))
                    else:
                        print(bcolors.RED + "[-]" + bcolors.END + " Invalid option '%s'" % key)
                else:
                    print("Usage: set <option> <value>")
            elif resp[:4] == 'code' and module is not None:
                if "showcode" in dir(module):
                    module.showcode()
                else:
                    print(status_warn % "code => This option is not enabled for this module")
            elif resp[:4] == 'test' and module is not None:
                if "test" in dir(module):
                    print(module.test())
                else:
                    print(status_warn % "test => This option is not enabled for this module")
            elif resp[:7] == 'options' and module is not None:
                module.show_options()
            elif resp[:4] == 'show':
                shopt = resp[5:]
                if shopt == 'trap':
                    showmodules()
            elif resp == 'trap':
                showmodules()
            elif resp[:3] == 'use':
                mod_path = resp[4:]
                if mod_path.isdigit() and len(modfiles) != 0:
                    mp_parts = modfiles[int(mod_path) - 1].split('/', 1)
                else:
                    mp_parts = mod_path.split('/', 1)
                if len(mp_parts) == 2:
                    try:
                        modstr = 'modules.%s.%s' % (mp_parts[0], mp_parts[1].replace('/', '.'))
                        pymod = importlib.import_module(modstr, package="polrbear")
                        module = pymod.PoLRModule()
                        module.init()
                        
                        strings.mod_type = mp_parts[0]
                        strings.mod_name = mp_parts[1]
                    except ImportError:
                        print(bcolors.RED + "[-]" + bcolors.END + " Invalid module '%s'" % mod_path)
                    


