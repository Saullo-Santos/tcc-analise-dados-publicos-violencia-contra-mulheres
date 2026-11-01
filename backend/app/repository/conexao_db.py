from os import getenv
from dotenv import load_dotenv
import pymysql


class ConexaoDB:
    def __init__(self):
        load_dotenv()
        self._server = getenv("DB_HOST")
        self._user = getenv("DB_USER")
        self._password = getenv("DB_PASSWORD")
        self._database = getenv("DB_NAME")
        self._conexao = None

    def _conectar(self):
        try:
            if self._conexao is None:
                self._conexao = pymysql.connect(host=self._server, user=self._user, password=self._password,database=self._database)
        
        except pymysql.DatabaseError as erro:
            raise Exception(erro)
        
        return self._conexao
        
    def cursor(self, sql, valores):
        cursor = None
        try:
            conexao = self._conectar()
            cursor = conexao.cursor()
            cursor.execute(sql, valores)
            conexao.commit()            
        except pymysql.DatabaseError as e:
            raise Exception(f"Erro: {e}")
        finally:
            if cursor:
                cursor.close()

    def desconectar(self):
        if self._conexao:
            self._conexao.close()
            self._conexao = None
    


