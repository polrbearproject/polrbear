
class PoLRCommand():

    def __init__(self, name):
        self.name = name
        self.namespace = 'None.Commands'
        self.using = ['System']

    def add_using(self, value):
        self.using.append[value]

    def add_code(self, code):
        self.code = code

    def create_class(self):
        clstxt = ''
        for u in self.using:
            clstxt += 'using %s;\n' % u
        
        clstxt += 'namespace %s\n{' % self.namespace
        clstxt += 'class %s\n{' % self.name
        clstxt += 'public %s(string[] args)\n{' % self.name
        clstxt += '%s\n}}}' % self.code

        return str(clstxt)
