#encoding: utf-8
from classes.modelos import *
# from dao import ConnectionFactoryPG
from dao.DAOs import  AtendenteDAO,FuncionarioDAO
from hashlib import md5

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
