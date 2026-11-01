import sys
from pathlib import Path
raiz = Path(__file__).resolve().parent.parent
sys.path.append(str(raiz))

from app.repository.conexao_db import ConexaoDB

class BaseDadosPublicoRepository(ConexaoDB):

    def inserir_multiplos_registros(self, lista_valores):
        """Método otimizado para inserir milhares de linhas de uma única vez"""
        cursor = None
        try:
            conexao = self._conectar()
            cursor = conexao.cursor()
            
            sql = """INSERT INTO registros 
                    (ano_bo, data_ocorrencia, hora_ocorrencia, natureza_crime, descr_tipo_local, bairro, logradouro, regiao, idade, cor_pele) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            # O executemany insere a lista completa em uma única transação ultra rápida
            cursor.executemany(sql, lista_valores)
            conexao.commit()
        except Exception as e:
            raise Exception(f"Erro na carga em lote do banco: {e}")
        finally:
            if cursor:
                cursor.close()
