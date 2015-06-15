from dao.ConnectionFactoryPG import *
from classes.modelos import *
from pprint import pprint
import pdb

class FuncionarioDAO(object):
    def save(self,func):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        if func.id == None:
            sql = "insert into funcionario(cpf,nome,salario) values (%s,%s,%s)"
            values = [func.cpf,func.nome,func.salario]
        else:
            sql = "update funcionario set nome = %s, salario = %s where cpf = %s "
            values = [func.nome,func.salario,func.cpf]
        try:
            # pdb.set_trace()
            cursor.execute(sql,values)
            func = self.findByCpf(func.cpf)
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
            if not bool(dicio):
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
            if not bool(dicio):
                func = None
            else:
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
        if not bool(client.id) :
            sql = "insert into cliente(telefone,nome,rua,bairro,complemento) \
                    values (%s,%s,%s,%s,%s)"
            values = [client.telefone,client.nome,
                        client.rua,client.bairro,client.complemento]
        else :
            sql = 'update cliente set telefone = %s, nome = %s, rua = %s, \
             bairro = %s, complemento = %s where id = %s '
            values = [client.telefone,client.nome,
                        client.rua,client.bairro,client.complemento,client.id]

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
        sql = "select * from cliente order by nome"
        try:
            cursor.execute(sql)
            dicio = cursor.fetchall()
            if not bool(dicio) :
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
            if not bool(dicio) :
                value = None
            else:
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
            if not bool(dicio):
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
        senha = atendente.senha
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
            if not bool(dicio):
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
            if not dicio:
                value = None
            else:
                value = Atendente(dict=dicio[0])
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
            value = cursor.execute(sql,values)
            value = self.find()[1][-1]
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
            if not bool(dicio):
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
            if not bool(dicio):
                value = None
            else:
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
            value = self.findByCnh(motoqueiro.cnh)
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
            if not bool(dicio):
                value = None
            else:
                value = self.map(dicio)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

    def findComNome(self):
        """ RETORNA DICIONARIO """
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from motoqueiro_com_nome"
        try:
            cursor.execute(sql)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = dicio
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
            if not bool(dicio):
                value = None
            else:
                value = Motoqueiro(dict=dicio[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

############# TELEFONE ############
class TelefoneDAO(object):
    def save(self,telefone):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "insert into telefone values (%s,%s)"
        values = [telefone.fcpf,telefone.numero]
        try:
            value = cursor.execute(sql,values)
            value = Motoqueiro(dict=value)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True, value

    def delete(self,numero):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "delete from telefone where numero = %s"
        values = [numero]
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
            c = Telefone(dict=i)
            l.append(c)
        return l

    def find(self):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from telefone"
        try:
            cursor.execute(sql)
            dicio = cursor.fetchall()
            if not bool(dicio):
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
        sql = "select * from telefone where numero like %s"
        values = ['%' + codigo + '%']
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = self.map(dicio[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

############# PEDIDO ##############
class PedidoDAO(object):
    def save(self,pedido):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "insert into pedido \
              (telefone_cliente,atendente_login, \
               entregue_por) \
                values (%s,%s,%s) "
        values = [pedido.telefone_cliente,
                 pedido.atendente_login,pedido.entregue_por]
        try:
            cursor.execute(sql,values)
            value = self.findByTelefoneCliente(pedido.telefone_cliente)[1][-1]
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True, value

    def delete(self,id):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = ["delete from item_pedido where pedido_id = %s","delete from pedido where id = %s"]
        values = [id]
        try:
            cursor.execute(sql[0],values)
            cursor.execute(sql[1],values)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False, e
        return True,None

    def map(self,values):
        l = []
        for i in values:
            c = Pedido(dict=i)
            l.append(c)
        return l

    def find(self):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from pedido"
        try:
            cursor.execute(sql)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = self.map(dicio)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value


    def findComNomes(self):
        """ Essa função retorna um dicionário com os resultados da
        VIEW 'pedidos_com_nomes' """
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "select * from pedidos_com_nomes"
        try:
            cursor.execute(sql)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = dicio
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

    def findById(self,id_code):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from pedido where id = %s"
        values = [id_code]
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = Pedido(dict=dicio[0])
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

    def findByTelefoneCliente(self,telefone_cliente):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from pedido where telefone_cliente like %s"
        values = [telefone_cliente]
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = self.map(dicio)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

############# ITEM_PEDIDO ##############
class Item_PedidoDAO(object):
    def save(self,item_pedido):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "insert into item_pedido \
                values (%s,%s,%s)"
        values = [item_pedido.pedido_id,item_pedido.prato_codigo,
                 item_pedido.qtd]
        try:
            cursor.execute(sql,values)
            value = self.findByPedidoAndPrato(item_pedido.pedido_id,item_pedido.prato_codigo)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True, value

    def delete(self,pedido_id,prato_codigo):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor()
        sql = "delete from item_pedido \
                where pedido_id = %s and prato_codigo = %s"
        values = [prato_codigo,pedido_id]
        print(values)
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
            c = Item_pedido(dict=i)
            l.append(c)
        return l

    def find(self):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from item_pedido"
        try:
            cursor.execute(sql)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = self.map(dicio)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

    def findByPedido(self,id_pedido):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from pegar_items_do_pedido(%s)"
        values = [id_pedido]
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = self.map(dicio)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value

    def findByPedidoAndPrato(self,id_pedido,codigo_prato):
        conn = ConnectionFactoryPG.getConnection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "select * from item_pedido p where p.pedido_id = %s and p.prato_codigo = %s "
        values = [id_pedido,codigo_prato]
        try:
            cursor.execute(sql,values)
            dicio = cursor.fetchall()
            if not bool(dicio):
                value = None
            else:
                value = self.map(dicio)
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(e.pgerror)
            return False,e.pgerror
        return True,value
