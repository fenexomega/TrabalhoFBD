from dao.ConnectionFactoryPG import *
from classes.modelos import *
from pprint import pprint

class FuncionarioDAO(object):
    def save(self,func):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "insert into funcionario values (%s,%s,%s)"
        values = [func.cpf,func.nome,func.salario]
        try:
            func = cursor.execute(sql,values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,func

    def delete(self,cpf):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "delete from funcionario where cpf = %s"
        values = [cpf]
        try:
            cursor.execute(sql,values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,cpf
        return True,None

    def map(self,values):
        l = []
        for i in values:
            f = Funcionario(dict=i)
            l.append(f)
        return l

    def find(self):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from funcionario"
        try:
            cursor.execute(sql)
            dicio = cursor.fetchall()
            if dicio == None:
                func = None
            else:
                func = self.map(dicio)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,func

    def findByCpf(self,cpf):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from funcionario where cpf = %s"
        values = [cpf]
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if dicio == None:
                func = None
            else:
                pprint(dicio)
                func = Funcionario(dict=dicio[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,func


################# CLIENT ######################
class ClienteDAO(object):
    def save(self,client):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "insert into cliente(telefone,nome,rua,bairro,complemento) \
                values (%s,%s,%s,%s,%s)"
        values = [client.telefone,client.nome,
                    client.rua,client.bairro,client.complemento]
        try:
            value = cursor.execute(sql,values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True, value

    def delete(self,telefone):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "delete from cliente where telefone = %s"
        values = [telefone]
        try:
            cursor.execute(sql,values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,cpf
        return True,None

    def map(self,values):
        l = []
        for i in values:
            c = Cliente(dict=i)
            l.append(c)
        return l

    def find(self):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from cliente"
        try:
            cursor.execute(sql)
            dicio = cursor.fetchall()
            if dicio == None:
                value = None
            else:
                value = self.map(dicio)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

    def findByTelefone(self,telefone):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from cliente where telefone = %s"
        values = [telefone]
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if dicio == None:
                value = None
            else:
                pprint(dicio)
                value = Cliente(dict=dicio[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

    def findByNome(self,nome):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from cliente where nome like %s"
        values = ['*' + nome + '*']
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if dicio == None:
                value = None
            else:
                pprint(dicio)
                value = Cliente(dict=dicio[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value
