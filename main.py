# from dao.ConnectionFactory import *
from dao.ConnectionFactoryPG import *
from pprint import pprint
from classes.modelos import *

def main():
    cursor = ConnectionFactoryPG.getConnection("deliverydb")
    cursor.execute("select * from cliente")
    l = cursor.fetchall()
    c = cliente(l[0])
    print(c)


if __name__ == "__main__":
    main()
