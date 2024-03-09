from src.tratamento_dados import tratar_dados_instantaneos
from src.insercao_db import inserir_dados
from teste import teste

retorno = tratar_dados_instantaneos()
inserir_dados(retorno)

