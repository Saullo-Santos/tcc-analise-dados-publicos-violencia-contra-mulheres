from fastapi import FastAPI, HTTPException, APIRouter
from app.repository.base_dados_publicas_repository import BaseDadosPublicoRepository

class DashboardAPIController:
    def __init__(self):
        self.router = APIRouter(prefix="/api", tags=["Análises TCC"])
        self.repo = BaseDadosPublicoRepository()
        self._registrar_rotas()

    def _registrar_rotas(self):
        @self.router.get("/registros/ano/{ano}")
        def buscar_por_ano(ano: int):
            try:
                dados = self.repo.buscar_registros_ano(ano)
                return {"ano": ano, "total": len(dados), "dados": dados}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get("/analises/faixa-etaria")
        def analise_faixa_etaria():
            try:
                resultado = self.repo.calculando_quantos_registros_tivemos_agrupando_por_idade()
                return [{"ano_bo": r[0], "faixa_etaria": r[1], "total_ocorrencias": r[2]} for r in resultado]
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get("/filtros/naturezas-crime")
        def listar_naturezas_crime():
            try:
                return {"naturezas": self.repo.tipos_de_natureza_crime()}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get("/analises/natureza-crime/{ano}")
        def analise_por_natureza(ano: int):
            try:
                resultado = self.repo.calculando_quantos_registros_para_cada_natureza_crime((ano,))
                return [{"natureza_crime": r[0], "total_ocorrencias": r[1]} for r in resultado]
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get("/analises/tipos-lugares/{ano}")
        def analise_tipos_lugares(ano: int):
            try:
                resultado = self.repo.tipos_de_lugares((ano,))
                return [{"descr_tipo_local": r[0], "total_ocorrencias": r[1]} for r in resultado]
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get("/filtros/cores-pele")
        def listar_cores_pele():
            try:
                return {"cores_pele": self.repo.cores_pele_vitimas()}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get("/analises/cor-pele/{ano}")
        def analise_cor_pele(ano: int):
            try:
                resultado = self.repo.calculando_soma_registros_por_cor_pele_ano((ano,))
                return [{"cor_pele": r[0], "total_casos": r[1]} for r in resultado]
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.router.get("/analises/periodo-dia/{ano}")
        def analise_periodo_dia(ano: int):
            try:
                resultado = self.repo.analisando_qual_pediodo_dia_mais_perigoso((ano,))
                return [{"ano_bo": r[0], "periodo_dia": r[1], "total_registros": r[2]} for r in resultado]
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))