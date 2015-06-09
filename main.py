# from dao.ConnectionFactory import *
from dao.ConnectionFactoryPG import *
from pprint import pprint

def main():
    cursor = ConnectionFactoryPG.getConnection("empresadb")
    cursor.execute("select * from funcionario")
    l = cursor.fetchall()
    pprint(l)


if __name__ == "__main__":
    main()
