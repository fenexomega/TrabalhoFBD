#encoding: utf-8
from classes.modelos import *
# from dao import ConnectionFactoryPG
from dao.DAOs import  *
from hashlib import md5
from prettytable import PrettyTable

def getMd5(string):
    md = md5(string.encode())
    return md.hexdigest()


def login(**kargs):
    if len(kargs) < 2:
        e = 'Parâmetros insuficientes\n'
        print(e)
        return False,e

    dao = AtendenteDAO()
    atendente = dao.findByLogin(login=kargs['login'])[1]
    if atendente == None :
        e = 'Login não existe\n'
        print(e)
        return False,e

    param_senha = getMd5(kargs['senha'])
    if param_senha == atendente.senha :
        fdao = FuncionarioDAO()
        funcionario = fdao.findByCpf(atendente.fcpf)[1]
        return True,atendente,funcionario
    e = 'Senha errada\n'
    print(e)
    return False,e

def listarCientes():
    dao = ClienteDAO()
    clients = dao.find()[1]
    x = PrettyTable(['id','Nome','Telefone','Rua','Bairro','Complemento'])
    x.align['Nome'] = x.align['Bairro'] = x.align['Rua'] = x.align['Complemento'] = 'l'
    x.align['id'] = 'r'
    n = 0
    for i in clients :
        n = n + 1
        x.add_row([n,i.nome,i.telefone,i.rua,i.bairro,i.complemento])
    print(x)
    return clients

def listarPedidos():
    dao = PedidoDAO()
    pedidos = dao.findComNomes()[1]
    x = PrettyTable(['id','Horário','Cliente','Atendente','Entregador','Total'])
    x.align['Horário'] = x.align['Cliente'] = x.align['Atendente'] = \
    x.align['Entregador'] = x.align['Total'] = 'l'
    x.align['id'] = 'r'
    for i in pedidos :
        x.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
    print(x)
    return pedidos
