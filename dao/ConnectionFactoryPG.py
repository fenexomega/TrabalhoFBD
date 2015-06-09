import psycopg2
import psycopg2.extras

class ConnectionFactoryPG:
    @staticmethod
    def getConnection(dbname,user = "postgres",host = "localhost"):
        conn = psycopg2.connect("\
            dbname='%s'\
            user='%s'\
            host=%s\
            " % (dbname,user,host)
            );
        # Se eu não pôr essa linha, a sessão nunca será fechada
        # automáticamente e eu teria de pôr .commit ou
        # .rollback a cada transação
        conn.autocommit = True
        # Para devolver as linhas do BD como dicionários
        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return c
