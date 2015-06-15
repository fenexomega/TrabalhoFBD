#encoding: utf-8
import classes.processos
import getpass
from dao import DAOs
from settings import *
from classes.modelos import *
from dao.DAOs import *
import hashlib

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
        print("Bem-vindo ao DeliverySys v%s" % Version)
        username = input("Digite seu login: ")
        senha = getpass.getpass("Digite sua senha: ")
        result = classes.processos.login(login=username,senha=senha)
        if result[0] :
            print('\n\nOlá, %s\n' % result[2].nome)
            return result
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

def perguntaPedidoPrato():
    text = """
    1-\tVer Pratos
    2-\tAdicionar Prato ao Pedido
    0-\tSair
    > """
    return intinput(text)

def perguntaFuncaoFuncionario():
    text = """Qual a função do funcionário?

    1-\tAtendente
    2-\tEntregador
    3-\tOutro

    > """
    return intinput(text)


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
    if dao.save(cliente)[0]:
        print("Cliente Salvo")
        return True,cliente
    print("Cliente não salvo")
    return False,None

def adicionarPratoAoPedido(pedido_id):
    d = {}
    d['pedido_id'] = pedido_id
    opcao = 1
    while not opcao == 0:
        print("ID_PEDIDO = %s" % pedido_id)
        classes.processos.listarItemsDoPedido(pedido_id)
        opcao = perguntaPedidoPrato()
        if opcao == 1:
            classes.processos.listaPratos()
        elif opcao == 2:
            d['prato_codigo'] = intinput("Digite o código do prato: ")
            d['qtd'] = intinput("Digite a quantidade: ")
            item_pedido = Item_pedido(dict=d)
            dao = Item_PedidoDAO()
            result = dao.save(item_pedido)
            if result:
                print("Item salvo com sucesso")
                continue
            print("Item não foi salvo")


def realizarPedido():
    cliente_tel = input("Digite tel do cliente: ")
    dao = ClienteDAO()
    cliente = dao.findByTelefone(cliente_tel)[1]
    if cliente == None :
        print('Cliente não existe')
        print('Deseja Registrar o Cliente? ')
        opcao = pergunta()
        if opcao == 1:
            b,cliente = cadastrarCliente(telefone=cliente_tel)
            if not b:
                return
        else:
            return
    else:
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
    dao = PedidoDAO()
    b,pedido = dao.save(pedido)
    if b:
         print("Pedido Salvo")
         print("Deseja cadastrar items no pedido? ")
         opcao = pergunta()
         if opcao == 1 :
             adicionarPratoAoPedido(pedido.id)
         return
    print("Pedido não salvo")

def cadastrarPrato():
    d = {}
    d['codigo'] = None
    d['nome'] = input("Digite o nome: ")
    d['valor'] = input("Digite o valor: ")
    p = Prato(dict=d)
    dao = PratoDAO()
    if dao.save(p)[0]:
        print("Prato salvo com sucesso")
    else:
        print("Não foi possível salvar o prato")

def cadastrarAtendente(fcpf,login,senha):
    # FIXME se já tiver cadastrado o login, só
    # mudar a senha
    dao = AtendenteDAO()
    senha = hashlib.md5(senha.encode()).hexdigest()
    d = {'fcpf':fcpf,'login':login,'senha':senha}
    at = Atendente(dict=d)
    dao.save(at)

def cadastrarEntregador(fcpf,cnh):
    dao = MotoqueiroDAO()
    d = {'fcpf':fcpf}
    moto = Motoqueiro(d)
    dao.save(moto)

def cadastrarFuncionario():
    d = {}
    d['id'] = None
    d['nome'] = ''
    d['salario'] = ''
    d['cpf'] = input("Digite o cpf: ")
    dao = FuncionarioDAO()
    func = dao.findByCpf(d['cpf'])[1]
    if func != None:
        print("O CPF %s pertence ao funcionário %s\n    Deseja atualizar? " % (func.cpf,func.nome))
        opcao = pergunta()
        d['id'] = func.id
        if opcao != 1:
            return
    else:
        func = Funcionario(dict=d)
    d['nome'] = input("Digite nome%s: " % (placeholder(func.nome))) or func.nome
    d['salario'] = input("Digite salário%s: " % (placeholder(func.salario))) or func.salario
    func = Funcionario(dict=d)
    rest = dao.save(func)[0]
    if rest:
        print("Funcionário Salvo")
        opcao = perguntaFuncaoFuncionario()
        if opcao == 1 :
            sucesso = False
            while not sucesso:
                login = input("Digite o seu login: ")
                senha1 = getpass.getpass("Digite sua senha: ")
                senha2 = getpass.getpass("Confirme sua senha: ")
                if senha1 != senha2:
                    print("\nErro: senha não confere!\n")
                    continue
                sucesso = True
                cadastrarAtendente(func.cpf,login,senha1)
        if opcao == 2:
            # FIXME caso de já existir o motoqueiro
            # peça pra digitar de novo
            cnh = input("Digite o CNH: ")
            cadastrarEntregador(func.cpf,cnh)
    else:
        print("Funcionário não salvo")
        # TODO CADASRAR E VER O TELEFONE




def subOpcoesPedido():
    text = """
    1-\tAdicionar Prato
    2-\tRemover Prato
    3-\tRemover Pedido
    0-\tSair

    > """
    return intinput(text)

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
    7-\tListar Pratos
    8-\tListar Funcionarios
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
        # CADSTRAR CLIENTE
        if i == 1 :
            cadastrarCliente()
        # CADASTRAR PEDIDO
        elif i == 2 :
            realizarPedido()
        # LISTAR CLIENTES
        elif i == 3 :
            clientes =  classes.processos.listarCientes()
            if subOpcoesAtualizacao() == 1:
                opcao = intinput("Digite o id: ")
                cadastrarCliente(clientes[opcao - 1])
        # PROCURAR CLIENTES
        elif i == 4 :
            dao = ClienteDAO()
            nome = input("Digite nome ou parte: ")
            clientes = dao.findByNome(nome)[1]
            classes.processos.listarCientes(clientes)
            if subOpcoesAtualizacao() == 1:
                opcao = intinput("Digite o id: ")
                cadastrarCliente(clientes[opcao - 1])
        # PROCURAR PEDIDO
        elif i == 5 :
            classes.processos.listarPedidos()
            print("Ver items do pedido?")
            opcao = pergunta()
            if opcao == 1:
                pedido = int(input("Digite id: "))
                classes.processos.listarItemsDoPedido(pedido)
                print("Deseja fazer alguma operação?")
                opcao =  subOpcoesPedido()
                if opcao == 1:
                    adicionarPratoAoPedido(pedido)
                elif opcao == 2:
                    opcao = int(input("Digite id do prato: "))
                    classes.processos.removerItemPedido(pedido,opcao)
                elif opcao == 3:
                    classes.processos.removerPedido(pedido)
        # CADASTRAR PRATO
        elif i == 6:
            cadastrarPrato()
        # LISTAR PRATOS
        elif i == 7:
            classes.processos.listaPratos()
        # LISTAR FUNCIONARIO
        elif i == 8:
            classes.processos.listarFuncionario()
        # CADASTRAR FUNCIONARIOS
        elif i == 9:
            cadastrarFuncionario()
        i = opcoes()
