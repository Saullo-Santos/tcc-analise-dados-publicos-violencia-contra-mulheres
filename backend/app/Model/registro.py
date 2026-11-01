from datetime import date
from time import time

class Registro:
    def __init__(self,ano_bo, data_ocorrencia, hora_ocorrencia, natureza_crime, descr_tipo_local, bairro, logradouro, regiao, idade, cor_pele):
        self._ano_bo = ano_bo
        try:
            if hasattr(data_ocorrencia, 'year'):
                self._data_ocorrencia = date(data_ocorrencia.year, data_ocorrencia.month, data_ocorrencia.day)
            else:
                self._data_ocorrencia = data_ocorrencia
        except:
            self._data_ocorrencia = ""
        
        try:
            if hasattr(hora_ocorrencia, 'hour'):
                self._hora_ocorrencia = time(hora_ocorrencia.hour, hora_ocorrencia.minute, hora_ocorrencia.second)
            else:
                self._hora_ocorrencia = hora_ocorrencia
        except Exception:
            self._hora_ocorrencia = ""

        self._natureza_crime = natureza_crime
        self._descr_tipo_local = descr_tipo_local
        self._bairro = bairro
        self._logradouro = logradouro
        self._regiao = regiao
        try:
            self._idade = int(idade)
        except:
            self._idade = ""
            
        self._cor_pele = cor_pele

    @property
    def ano_bo(self):
        return self._ano_bo

    @property
    def data_ocorrencia(self):
        return self._data_ocorrencia

    @property
    def hora_ocorrencia(self):
        return self._hora_ocorrencia

    @property
    def natureza_crime(self):
        return self._natureza_crime

    @property
    def descr_tipo_local(self):
        return self._descr_tipo_local

    @property
    def bairro(self):
        return self._bairro

    @property
    def logradouro(self):
        return self._logradouro

    @property
    def regiao(self):
        return self._regiao

    @property
    def idade(self):
        return self._idade

    @property
    def cor_pele(self):
        return self._cor_pele



