#encoding: utf-8
import classes.processos
import getpass
from dao import DAOs
from settings import *
from classes.modelos import *
from dao.DAOs import *

intinput = lambda s: int(input(s))

def placeholder(st):
    if st == '':
        return st
    return "[%s]" % st


# REMOVER PEDIDO
# FAZER PEDIDO
# CRUD CLIENTE
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



def pergunta():
    text = """
    1-\tSim
    0-\tNão

    > """
    i = input(text)
    return int(i)

def cadastrarCliente(cliente = None,**kargs):
    dictionary = {}
    if cliente == None:
        cliente = Cliente()
        cliente.id            = None
        cliente.telefone      = (kargs.get('telefone') and kargs['telefone']) or ''
        cliente.nome          = ''
        cliente.rua           = ''
        cliente.bairro        = ''
        cliente.complemento   = ''
    dictionary['id']            = cliente.id
    dictionary['nome']          = input("Digite nome%s: " % (placeholder(cliente.nome))) or cliente.nome
    dictionary['telefone']      = input("Digite telefone%s: " % (placeholder(cliente.telefone))) or cliente.telefone
    dictionary['rua']           = input("Digite rua%s: " % (placeholder(cliente.rua))) or cliente.rua
    dictionary['bairro']        = input("Digite bairro%s: " % (placeholder(cliente.bairro))) or cliente.bairro
    dictionary['complemento']   = input("Digite complemento%s: " % (placeholder(cliente.complemento))) or cliente.complemento
    cliente = Cliente(dict=dictionary)
    dao = ClienteDAO()
    if dao.save(cliente):
        print("Cliente Salvo")
        return True
    print("Cliente não salvo")
    return False



def realizarPedido():
    cliente_tel = input("Digite tel do cliente: ")
    dao = ClienteDAO()
    cliente = dao.findByTelefone(cliente_tel)[1]
    if cliente == None :
        print('Cliente não existe')
        print('Deseja Registrar o Cliente? ')
        opcao = pergunta()
        if opcao == 1:
            if not cadastrarCliente(telefone=cliente_tel):
                return
        else:
            return
    opcao = input("Cliente %s, correto? [s/n]" % cliente.nome)
    if str.upper(opcao[0]) == 'N':
        return
    d = {}
    d['id'] = None
    d['horario_pedido'] = None
    d['telefone_cliente'] = cliente.telefone
    d['atendente_login'] = usuario.login
    d['valor_total'] = None
    motos = classes.processos.listarEntregadores()
    opcao = intinput("Selecione o entregador (id): ")
    d['entregue_por'] = motos[opcao - 1]['cnh']
    pedido = Pedido(dict=d)
    # TODO aqui tá imprimindo um None sem noção
    dao = PedidoDAO()
    if dao.save(pedido):
         print("Pedido Salvo")
         return
    print("Pedido não salvo")






def subOpcoesAtualizacao():
    text = """
    1-\tAtualizar
    0-\tSair

    > """
    i = intinput(text)
    return i

def opcoes():
    text = """
##### MENU #####

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

def main():
    global usuario
    usuario = login()[1]
    if not usuario :
        return

    i = opcoes()
    while i != 0:
        if i == 1 :
            cadastrarCliente()
        elif i == 2 :
            realizarPedido()
        elif i == 3 :
            clientes =  classes.processos.listarCientes()
            if subOpcoesAtualizacao() == 1:
                opcao = intinput("Digite o id: ")
                cadastrarCliente(clientes[opcao - 1])
        elif i == 4 :
            dao = ClienteDAO()
            nome = input("Digite nome ou parte: ")
            clientes = dao.findByNome(nome)[1]
            classes.processos.listarCientes(clientes)
            if subOpcoesAtualizacao() == 1:
                opcao = intinput("Digite o id: ")
                cadastrarCliente(clientes[opcao - 1])
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
