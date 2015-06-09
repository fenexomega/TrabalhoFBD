#!/usr/bin/env python

class ConnectionFactory():
    @staticmethod
    def getConnection(dbname,user = "postgres",host = "localhost"):
        raise NotImplementedError("Função não implementada")
