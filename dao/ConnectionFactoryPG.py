import psycopg2
import psycopg2.extras
from settings import dbsettings

class ConnectionFactoryPG:
    @staticmethod
    def getConnection():
        conn = psycopg2.connect("\
            dbname='%s'\
            user='%s'\
            host=%s\
            password=%s\
            " % (
                 dbsettings['database'],
                 dbsettings['user'],
                 dbsettings['host'],
                 dbsettings['password'])
                );
        # Se eu não pôr essa linha, a sessão nunca será fechada
        # automáticamente e eu teria de pôr .commit ou
        # .rollback a cada transação
        conn.autocommit = True
        # Para devolver as linhas do BD como dicionários
        #c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return conn
