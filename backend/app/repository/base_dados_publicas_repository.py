import sys
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
sys.path.append(str(raiz))

from app.repository.conexao_db import ConexaoDB
from app.Model.registro import Registro



class BaseDadosPublicoRepository(ConexaoDB):


    def inserir_registro(self, registro:Registro):
        try:
            sql = """INSERT INTO registros 
                    (ano_bo, data_ocorrencia, hora_ocorrencia, natureza_crime, descr_tipo_local, bairro, logradouro, regiao, idade, cor_pele) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            valores = (registro.ano_bo, registro.data_ocorrencia, registro.hora_ocorrencia, registro.natureza_crime, registro.descr_tipo_local, registro.bairro,
                       registro.logradouro, registro.regiao, registro.idade, registro.cor_pele)



            self.cursor(sql, valores)

        except:
            raise Exception()





