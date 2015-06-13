xstr = lambda s: s or ''

class Funcionario(object):
    def __init__(self,**kargs):
        if len(kargs) == 0:
            return
        if kargs.get('dict') != None :
            self.cpf     = kargs['dict']['cpf']
            self.nome    = kargs['dict']['nome']
            self.salario = kargs['dict']['salario']
            return
        self.cpf     = kargs['cpf']
        self.nome    = kargs['nome']
        self.salario = kargs['salario']



class Cliente(object):
    def __init__(self,**kargs):
        if len(kargs) == 0:
            return
        if kargs.get('dict') != None :
            self.telefone    = kargs['dict']['telefone']
            self.nome        = kargs['dict']['nome']
            self.rua         = kargs['dict']['rua']
            self.bairro      = kargs['dict']['bairro']
            self.complemento = xstr(kargs['dict']['complemento'])
            return
        self.telefone    = kargs['telefone']
        self.nome        = kargs['nome']
        self.rua         = kargs['rua']
        self.bairro      = kargs['bairro']
        self.complemento = xstr(kargs['complemento'])
    def __str__(self):
        return '[{},{},{},{},{}]'.format(self.telefone,str(self.aniversario.day) + "/" + str(self.aniversario.month) + "/" + str(self.aniversario.year),self.nome,
        self.rua,self.bairro,str(self.complemento))
    def __unicode__(self):
        return u'[{},{},{},{},{}]'.format(self.telefone,str(self.aniversario.day) + "/" + str(self.aniversario.month) + "/" + str(self.aniversario.year),self.nome,
        self.rua,self.bairro,str(self.complemento))

class Atendente(object):
    def __init__(self):
        pass

    def __init__(self,**kargs):
        if len(kargs) == 0:
            return
        if kargs.get('dict') != None :
            self.fcpf = kargs['dict']['fcpf']
            self.login = kargs['dict']['login']
            self.senha = kargs['dict']['senha']
            return
        self.fcpf = kargs['fcpf']
        self.login = kargs['login']
        self.senha = kargs['senha']

class Prato(object):
    def __init__(self):
        pass

    def __init__(self,**kargs):
        if len(kargs) == 0:
            return
        if kargs.get('dict') != None :
            self.codigo = kargs['dict']['codigo']
            self.nome = kargs['dict']['nome']
            self.valor = kargs['dict']['valor']
            return
        self.codigo = kargs['codigo']
        self.nome = kargs['nome']
        self.valor = kargs['valor']

class Motoqueiro(object):
    def __init__(self):
        pass

    def __init__(self,**kargs):
        if len(kargs) == 0:
            return
        if kargs.get('dict') != None :
            self.fcpf = kargs['dict']['fcpf']
            self.cnh = kargs['dict']['cnh']
            return
        self.fcpf = kargs['fcpf']
        self.cnh = kargs['cnh']

class Telefone(object):
    def __init__(self):
        pass

    def __init__(self,**kargs):
        if len(kargs) == 0:
            return
        if kargs.get('dict') != None :
            self.fcpf = kargs['dict']['fcpf']
            self.numero = kargs['dict']['numero']
            return
        self.fcpf = kargs['fcpf']
        self.numero = kargs['numero']

class Pedido(object):
    def __init__(self):
        pass

    def __init__(self,**kargs):
        if len(kargs) == 0:
            return
        if kargs.get('dict') != None :
            self.id = kargs['dict']['id']
            self.horario_pedido = kargs['dict']['horario_pedido']
            self.telefone_cliente = kargs['dict']['telefone_cliente']
            self.atendente_login = kargs['dict']['atendente_login']
            self.entregue_por = kargs['dict']['entregue_por']
            self.valor_total = kargs['dict']['valor_total']
            return
        self.id = kargs['id']
        self.horario_pedido = kargs['horario_pedido']
        self.telefone_cliente = kargs['telefone_cliente']
        self.atendente_login = kargs['atendente_login']
        self.entregue_por = kargs['entregue_por']
        self.valor_total = kargs['valor_total']

class Item_pedido(object):
    def __init__(self):
        pass

    def __init__(self,**kargs):
        if len(kargs) == 0:
            return
        if kargs.get('dict') != None :
            self.pedido_id = kargs['dict']['pedido_id']
            self.prato_codigo = kargs['dict']['prato_codigo']
            self.qtd = kargs['dict']['qtd']
        self.pedido_id = kargs['pedido_id']
        self.prato_codigo = kargs['prato_codigo']
        self.qtd = kargs['qtd']
