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
            # Dica: Use caminhos relativos ao projeto ou absolutos para não se perder dependendo de onde roda
            return pd.read_excel("backend/base_dados_publicos/Base_Violencia_contra_mulher.xlsx", sheet_name="BASE_VD")
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo Excel não encontrado no caminho especificado")

    def realizar_segmentacao_salvar_banco_dados(self):
        try:
            data_frame = self.abrir_Base()
            lote_dados = []
            data_frame = data_frame.astype(object).where(pd.notnull(data_frame), None)
            repo = BaseDadosPublicoRepository()

            for _, registro in data_frame.iterrows():
                registro_objeto = Registro(
                    ano_bo=registro["ANO_BO"],
                    data_ocorrencia=registro["DATA_OCORRENCIA_BO"],
                    hora_ocorrencia=registro["HORA_OCORRENCIA_BO"],
                    natureza_crime=registro["NATUREZA_APURADA"],
                    descr_tipo_local=registro["DESCR_TIPOLOCAL"],
                    bairro=registro["BAIRRO"],
                    logradouro=registro["LOGRADOURO"],
                    regiao=None,
                    idade=registro["IDADE_PESSOA"],
                    cor_pele=registro["COR_CUTIS"]
                )

                valores = (
                    registro_objeto.ano_bo, registro_objeto.data_ocorrencia, registro_objeto.hora_ocorrencia,
                    registro_objeto.natureza_crime, registro_objeto.descr_tipo_local, registro_objeto.bairro,
                    registro_objeto.logradouro, registro_objeto.regiao, registro_objeto.idade, registro_objeto.cor_pele
                )
                lote_dados.append(valores)

            if lote_dados:
                print(f"Enviando {len(lote_dados)} registros para o MySQL...")
                repo.inserir_multiplos_registros(lote_dados)
                repo.desconectar()

        except Exception as err:
            raise Exception(f"Falha no processamento: {err}")

if __name__ == "__main__":
    # t = TratatamentoBaseDadosPublicos()
    # try:
    #     print("Executando código...")
    #     t.realizar_segmentacao_salvar_banco_dados()
    #     print("Terminou! Confere aí no banco de dados.")
    # except Exception as e:
    #     print(f"Ocorreu um erro no pipeline: {e}")


    Teste = BaseDadosPublicoRepository()
    # print(Teste.calculando_quantos_registros_tivemos_agrupando_por_idade())
    # print(Teste.tipos_de_natureza_crime())
    # print(Teste.calculando_quantos_registros_para_cada_natureza_crime(2026))
    # print(Teste.tipos_de_lugares(2024))
    # print(Teste.cores_pele_vitimas())
    # print(Teste.calculando_soma_registros_por_cor_pele_ano(2025))
    print(Teste.analisando_qual_pediodo_dia_mais_perigoso(2025))