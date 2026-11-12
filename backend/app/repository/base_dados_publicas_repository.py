import sys
from pathlib import Path
raiz = Path(__file__).resolve().parent.parent
sys.path.append(str(raiz))

from app.repository.conexao_db import ConexaoDB

class BaseDadosPublicoRepository(ConexaoDB):

    def _estrutura_de_execucao_consulta(self, query, parametros=None):
        cursor = None
        try:
            conexao = self._conectar()
            cursor = conexao.cursor()

            cursor.execute(query, parametros)
            return cursor.fetchall()
            
        except Exception as e:
            raise Exception(f"Erro na consulta ao banco: {e}")
        finally:
            if cursor:
                cursor.close()

            self.desconectar()
    
    
    def inserir_multiplos_registros(self, lista_valores):
        """Método otimizado para inserir milhares de linhas de uma única vez"""
        cursor = None
        try:
            conexao = self._conectar()
            cursor = conexao.cursor()
            
            sql = """INSERT INTO registros 
                    (ano_bo, data_ocorrencia, hora_ocorrencia, natureza_crime, descr_tipo_local, bairro, logradouro, regiao, idade, cor_pele) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            cursor.executemany(sql, lista_valores)
            conexao.commit()
        except Exception as e:
            raise Exception(f"Erro na carga em lote do banco: {e}")
        finally:
            if cursor:
                cursor.close()
    

    def buscar_registros_ano(self, ano):
        query = """SELECT * FROM registros WHERE ano_bo = %s"""
        try:
            return self._estrutura_de_execucao_consulta(query, (ano,))
        except Exception as e:
            raise Exception(f"Erro na execução: {e}")

    # def calculando_quantos_registros_tivemos_agrupando_por_idade(self):
    #     query = """SELECT 
    #         ano_bo,
    #         CASE 
    #             WHEN idade < 18 THEN 'Menores de 18'
    #             WHEN idade BETWEEN 18 AND 60 THEN '18 a 60 anos'
    #             ELSE 'Maior de 60'
    #         END AS faixa_etaria,
    #         COUNT(*) AS total_ocorrencias
    #         FROM registros
    #         WHERE ano_bo IN (2024, 2025, 2026)
    #         GROUP BY ano_bo, faixa_etaria
    #         ORDER BY ano_bo ASC, faixa_etaria;"""

    #     try:
    #         return self._estrutura_de_execucao_consulta(query)
    #     except Exception as e:
    #         raise Exception(f"Erro na execução: {e}")


    def calculando_quantos_registros_tivemos_agrupando_por_idade(self):
        query = """SELECT 
        ano_bo,
        CASE 
            WHEN idade IS NULL THEN 'Não informado'
            WHEN idade < 18 THEN 'Menores de 18'
            WHEN idade BETWEEN 18 AND 60 THEN '18 a 60 anos'
            ELSE 'Maior de 60'
        END AS faixa_etaria,
        COUNT(*) AS total_ocorrencias
        FROM registros
        WHERE ano_bo IN (2024, 2025, 2026)
        GROUP BY ano_bo, faixa_etaria
        ORDER BY ano_bo ASC, MIN(idade) ASC;"""

        try:
            return self._estrutura_de_execucao_consulta(query)
        except Exception as e:
            raise Exception(f"Erro na execução: {e}")

    def tipos_de_natureza_crime(self):
        query = "SELECT DISTINCT natureza_crime FROM registros ORDER BY natureza_crime ASC;"
        try:
            return self._estrutura_de_execucao_consulta(query) #ajustar a forma de como os dados retornam.
        except Exception as e:
            raise Exception(f"Erro na execução: {e}")