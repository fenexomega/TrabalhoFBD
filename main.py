# from dao.ConnectionFactory import *
from dao.ConnectionFactoryPG import *
from pprint import pprint
from classes.modelos import *
from dao.DAOs import *

def main():
    cursor = ConnectionFactoryPG.getConnection()
    cursor.execute("select * from cliente")
    l = cursor.fetchall()
    c = cliente(l[0])
    print(c)

def testFunc():
    dao = FuncionarioDAO()
    func = Funcionario(cpf='12300012300',nome='Chapa de Teste',salario=2391.00)
    dao.save(func)
    # print(dao.delete('12300012300'))
    print(dao.find())
def testCliente():
    dao = ClienteDAO()
    c = Cliente(telefone='999999999',nome='Thomas Turbano',
    rua='Rua aracapé 234',bairro='Bairro 3',complemento=None)
    dao.save(c)
    pprint(dao.findByNome('Th'))

if __name__ == "__main__":
    testFunc()
    testCliente()
