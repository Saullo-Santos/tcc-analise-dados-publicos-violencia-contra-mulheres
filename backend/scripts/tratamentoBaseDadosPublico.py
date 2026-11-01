import pandas as pd

import sys
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent
sys.path.append(str(raiz))

from app.Model.registro import Registro
from app.repository.base_dados_publicas_repository import BaseDadosPublicoRepository


class TratatamentoBaseDadosPublicos:

    def abrir_Base(self):
        try:
            self._data_frame = pd.read_excel("backend/base_dados_publicos/Base_Violencia_contra_mulher.xlsx", sheet_name="BASE_VD")
            return self._data_frame
        
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo Excel não encontrado")

    def realizar_segmentacao_salvar_banco_dados(self):
        try:
            data_frame = self.abrir_Base()

            for _, registro in data_frame.iterrows():
                ano_bo = registro["ANO_BO"]
                hora_ocorrencia = registro["HORA_OCORRENCIA_BO"]
                data_ocorrencia = registro["DATA_OCORRENCIA_BO"]
                natureza_crime = registro["NATUREZA_APURADA"]
                descr_tipo_local = registro["DESCR_TIPOLOCAL"]
                bairro = registro["BAIRRO"]
                logradouro = registro["LOGRADOURO"]
                regiao = registro["ANO_BO"]
                idade = registro["IDADE_PESSOA"]
                cor_pele = registro["COR_CUTIS"]
                registro_objeto = Registro(ano_bo, data_ocorrencia, hora_ocorrencia, natureza_crime, descr_tipo_local, bairro, logradouro, regiao, idade, cor_pele)
                try:
                    BaseDadosPublicoRepository.inserir_registro(registro_objeto)
                except:
                    raise Exception()

        except FileNotFoundError as err:
            raise FileNotFoundError(err)


t = TratatamentoBaseDadosPublicos()
try:
    print("Executando código")
    t.realizar_segmentacao_salvar_banco_dados()
    print("Terminou confere ai no banco de dados")

except Exception as e:
    print(e)


