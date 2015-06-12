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
        values = ['%' + nome + '%']
        try:
            cursor.execute(sql,values)
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

############### Atendente ################
class AtendenteDAO(object):
    def save(self,atendente):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "insert into atendente values (%s,%s,%s)"
        senha = md5(atendente.senha.encode()).hexdisgest()
        values = [atendente.fcpf,atendente.login,senha]
        try:
            value = cursor.execute(sql,values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True, value

    def delete(self,login):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "delete from atendente where login = %s"
        values = [login]
        try:
            cursor.execute(sql,values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,login
        return True,None

    def map(self,values):
        l = []
        for i in values:
            c = Atendente(dict=i)
            l.append(c)
        return l

    def find(self):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from atendente"
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

    def findByLogin(self,login):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from atendente where login = %s"
        values = [login]
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

####### PRATO ##########
class PratoDAO(object):
    def save(self,prato):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "insert into prato(nome,valor) values (%s,%s)"
        values = [prato.nome,prato.valor]
        try:
            value = cursor.execute(sql,values).fetchall()
            value = Prato(dict=value[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True, value

    def delete(self,codigo):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "delete from prato where codigo = %s"
        values = [codigo]
        try:
            cursor.execute(sql,values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,codigo
        return True,None

    def map(self,values):
        l = []
        for i in values:
            c = Prato(dict=i)
            l.append(c)
        return l

    def find(self):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from prato"
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

    def findByCodigo(self,codigo):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from prato where codigo = %s"
        values = [codigo]
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if dicio == None:
                value = None
            else:
                pprint(dicio)
                value = Prato(dict=dicio[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

########## MOTOQUEIRO ############
class MotoqueiroDAO(object):
    def save(self,motoqueiro):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "insert into motoqueiro values (%s,%s)"
        values = [motoqueiro.fcpf,motoqueiro.cnh]
        try:
            value = cursor.execute(sql,values)
            value = Motoqueiro(dict=value)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True, value

    def delete(self,fcpf):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "delete from motoqueiro where fcpf = %s"
        values = [fcpf]
        try:
            cursor.execute(sql,values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False, fcpf
        return True,None

    def map(self,values):
        l = []
        for i in values:
            c = Motoqueiro(dict=i)
            l.append(c)
        return l

    def find(self):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from motoqueiro"
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

    def findByCnh(self,cnh):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from motoqueiro where cnh like %s"
        values = ['%' + codigo + '%']
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if dicio == None:
                value = None
            else:
                pprint(dicio)
                value = Motoqueiro(dict=dicio[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value
