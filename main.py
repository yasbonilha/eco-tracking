from leitura_dados import ler_dados
#from tratamento_dados import tratar_dados_instantaneos, tratar_dados_permanentes
from insercao_db import inserir_dados

corrida = True
botao = False

while corrida == True:
    dados_crus= ler_dados()
    #dados_tratados = tratar_dados_instantaneos(dados_crus)
    
    if botao == True:
        #tratar_dados_permanentes()
        #inserir_dados(dados_tratados)
        corrida = False

