#encoding: utf-8
import classes.processos
import getpass
from dao import DAOs
from settings import *

usuario = None

def login():
    if not Debug :
        print("Bem-vindo ao DeliverySys v0.001a")
        username = input("Digite seu login: ")
        senha = getpass.getpass("Digite sua senha: ")
        result = classes.processos.login(login=username,senha=senha)
        if result[0] :
            print('Olá, %s\n\n' % result[2].nome)
            return result[1]
        return False
    else :
        return classes.processos.login(login='admin',senha='admin')

def opcoes():
    text = """
    1-\tCadastrar Cliente
    2-\tCadastrar Pedido
    3-\tListar Clientes
    4-\tProcurar Cliente
    5-\tProcurar Pedido
    6-\tCadastrar Prato
    7-\tProcurar Prato
    8-\tListar Funcionario
    9-\tCadastrar Funcionario
    0-\tSair

    > """
    i = input(text)
    return int(i)

def pergunta():
    text = """
    1-\tSim
    0-\tNão

    > """
    i = input(text)
    return int(i)



def realizarPedido():
    cliente_tel = input("Digite tel do cliente: ")
    dao = ClienteDAO()
    cliente = dao.findByTelefone(cliente_tel)[1]
    if cliente == None :
        print('Cliente não existe')
        print('Deseja Registrar o Cliente? ')
        opcao = pergunta()
        if opcao == 1:
            pass
        else:
            return
    d = {}
    d['telefone_cliente'] = cliente.telefone
    d['atendente_login'] = usuario.login
    d['valor_total'] = 0
    motos = classes.processos.listarEntregadores()
    opcao = input("Selecione o entregador (id): ")

    pedido = Pedido()




def subOpcoesAtualizacao():
    text = """
    1-\tAtualizar
    0-\tSair
    """
    i = input(text)
    return i

def main():
    global usuario
    usuario = login()
    if not usuario :
        return

    i = opcoes()
    while i != 0:
        if i == 1 :
            pass
        elif i == 2 :
            pass
        elif i == 3 :
            classes.processos.listarCientes()
            if subOpcoesAtualizacao() == 1:
                pass
        elif i == 5 :
            classes.processos.listarPedidos()
            print("Ver items do pedido?")
            opcao = pergunta()
            if opcao == 1:
                pedido = int(input("Digite id: "))
                classes.processos.listarItemsDoPedido(pedido)
                print("Deseja remover algum item?")
                opcao = pergunta()
                if opcao == 1:
                    opcao = int(input("Digite id do prato: "))
                    classes.processos.removerItemPedido(pedido,opcao)

        i = opcoes()
