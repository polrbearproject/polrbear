from conf import strings
from conf.strings import *

columns = {
    'key':{'header':'Name','size':10},
    'value':{'header':'Current Setting','size':15},
    'required':{'header':'Required','size':8},
    'description':{'header':'Description','size':75}
}

class Options:
    """ Primary Options Class """

    def __init__(self):
        self.options = {}

    def add_option(self, key, value, required=False, description=''):
        self.options.update({
            key.upper():{
                'value':value,
                'required':required,
                'description':description                
            }
        })

    def set_option(self, key, value):
        self.options[key.upper()]['value'] = value

    def get_option(self, key):
        return str(self.options[key.upper()]['value'])

    def is_option(self, key):
        return bool(key.upper() in self.options)

    def show_options(self):
        global headers
        spac = '    '
        line = spac
        sepr = spac

        # set the column spacing based on value length
        keylen = columns['key']['size']
        vallen = columns['value']['size']
        for k,v in sorted(self.options.items(), key=lambda t: t[0]):
            if(len(k)) > keylen:
                keylen = len(k)
            if len(v['value']) > vallen:
                vallen = len(v['value'])
        columns['key']['size'] = keylen
        columns['value']['size'] = vallen


        # print the header and separator line
        for k,v in columns.items():
            line += v['header'].ljust(v['size']) + '  '
            sepr += str('-' * len(v['header'])).ljust(v['size']) + '  '
        print(strings.mod_opt % ('trap/' + strings.mod_name))
        print(line)
        print(sepr)

        # print each option and values
        for k,v in sorted(self.options.items(), key=lambda t: t[0]):
            optline = spac          
            optline += k.ljust(columns['key']['size']) + '  '
            optline += str(v['value']).ljust(columns['value']['size']) + '  '
            optline += str(v['required']).ljust(columns['required']['size']) + '  '
            optline += str(v['description']).ljust(columns['description']['size']) + '  '
            print(optline)
        print('')
