#from src.tratamento_dados import tratar_dados_instantaneos, tratar_dados_permanentes
from src.insercao_db import inserir_dados
from src.tratamento_dados_teste import tratar_dados_instantaneos
import matplotlib.pyplot as plt

'''
chamamos o tratamento de dados, que recebe os dados automaticamente. inserimos os dados no banco de dados. tratamos os dados permanentes.
'''

retorno = tratar_dados_instantaneos()
# inserir_dados(retorno)
# tratar_dados_permanentes()

