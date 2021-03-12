class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    DARKCYAN = '\033[36m'
    WHITE = '\033[37m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'
    UNDERL = '\033[4m'

prompt_text = bcolors.GREEN + bcolors.UNDERL + 'polr' + bcolors.END
prompt_sep = ' > '
mod_type = ''
mod_name = ''
status_info = bcolors.BOLD + bcolors.BLUE + '[*]' + bcolors.END + ' %s'
status_warn = bcolors.BOLD + bcolors.RED + '[-]' + bcolors.END + ' %s'
status_okay = bcolors.BOLD + bcolors.GREEN + '[+]' + bcolors.END + ' %s'
status_detail = bcolors.YELLOW + '%s' + bcolors.END
status_title = bcolors.DARKCYAN + '%s' + bcolors.END

#module options
show_mod = '\nAvailable modules:\n'
shmod_header = '     Module'
shmod_hdrsep = '     ------'
shmod_line = ' %s   %s'
mod_opt = "\nModule options (%s):\n"

#none App Strings
write_line = 'Console.WriteLine(%s);\n'

def prompt():
    if mod_name == '':
        pstr = str(prompt_text + prompt_sep)
    else:
        pstr = str(prompt_text + ' ' + mod_type + '(' + bcolors.RED + mod_name + bcolors.END + ')' + prompt_sep)

    try:
        return input(pstr)
    except KeyboardInterrupt:
        print('')
        return None

version = '0.1-alpha'
codename = 'Yuri'

logo = """
██████╗  ██████╗ ██╗     ██████╗ ██████╗ ███████╗ █████╗ ██████╗ 
██╔══██╗██╔═══██╗██║     ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗
██████╔╝██║   ██║██║     ██████╔╝██████╔╝█████╗  ███████║██████╔╝
██╔═══╝ ██║   ██║██║     ██╔══██╗██╔══██╗██╔══╝  ██╔══██║██╔══██╗
██║     ╚██████╔╝███████╗██║  ██║██████╔╝███████╗██║  ██║██║  ██║
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

                      The PoLRBear Project                      
                       Created by: %s

""" % (bcolors.BOLD + bcolors.GREEN + 'ben0xa' + bcolors.END)

info_line = '             [ %s ]'
version_text = bcolors.BOLD + bcolors.WHITE + 'polrbear' + bcolors.END + ' - ' + bcolors.YELLOW + version + bcolors.END + ' (Codename: ' + bcolors.BOLD + bcolors.GREEN + codename + bcolors.END + ')'
version_line = info_line % version_text