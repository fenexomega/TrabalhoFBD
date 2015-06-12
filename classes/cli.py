#encoding: utf-8
import classes.processos
import getpass
from dao import DAOs

usuario = None

def login():
    print("Bem-vindo ao DeliverySys v0.001a")
    username = input("Digite seu login: ")
    senha = getpass.getpass("Digite sua senha: ")
    result = classes.processos.login(login=username,senha=senha)
    if result[0] :
        print('Olá, %s\n\n' % result[2].nome)
        return result[1]
    return False

def opcoes():
    text = """
    1-\tCadastrar Cliente
    2-\tCadastrar Pedido
    3-\tListar Clientes
    4-\tProcurar Cliente
    5-\tProcurar Pedido
    6-\tCadastrar Prato
    7-\tProcurar Prato
    8-\tProcurar Funcionario
    9-\tCadastrar Funcionario
    0-\tSair
    """
    i = input(text)
    return int(i)



def main():
    global usuario
    usuario = login()
    if not usuario :
        return

    i = opcoes()
    while i != 0:
        i = opcoes()
        if i == 1 :
            pass
        elif i == 2 :
            pass
        elif i == 3 :
