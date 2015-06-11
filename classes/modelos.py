class funcionario(object):
    def __init__(self,dict):
        self.cpf = dict['cpf']
        self.nome = dict['nome']
        self.salario = dict['salario']


class cliente(object):
    def __init__(self,dict):
        self.telefone = dict['telefone']
        self.aniversario = dict['aniversario']
        self.nome = dict['nome']
        self.rua = dict['rua']
        self.bairro = dict['bairro']
        self.complemento = dict['complemento']
    def __str__(self):
        return '[{},{},{},{},{}]'.format(self.telefone,str(self.aniversario.day) + "/" + str(self.aniversario.month) + "/" + str(self.aniversario.year),self.nome,
        self.rua,self.bairro,str(self.complemento))
    def __unicode__(self):
        return u'[{},{},{},{},{}]'.format(self.telefone,str(self.aniversario.day) + "/" + str(self.aniversario.month) + "/" + str(self.aniversario.year),self.nome,
        self.rua,self.bairro,str(self.complemento))
