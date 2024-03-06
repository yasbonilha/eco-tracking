#from leitura_dados import dicionario
from mock.mock_leitura_dados import dicionario
import pandas as pd


#dados instantâneos

print(dicionario)

# volta, tempo, velocidade, consumo, aceleracao, x, y, rpm
tabela = pd.DataFrame(columns = ["volta", "tempo", "velocidade", "consumo", "aceleracao", "x", "y", "rpm"])


def tratar_dados_instantaneos(dicionario):
    #TRATAMENTO DE TEMPO
    tabela.append(dicionario.volta, dicionario.tempo, dicionario.velocidade, dicionario.consumo, dicionario.aceleracao, dicionario.x, dicionario.y, dicionario.rpm)








#dados permanentes - calculados só no final da corrida


