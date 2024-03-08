#from leitura_dados import dicionario
from mock.mock_leitura_dados import dicionario
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation

#dados instantâneos

print(dicionario)

# volta, tempo, velocidade, consumo, aceleracao, x, y, rpm
tabela = pd.DataFrame(columns = ["volta", "tempo", "velocidade", "consumo", "aceleracao", "x", "y", "rpm"])


def tratar_dados_instantaneos(dicionario):
    tabela.append(dicionario.volta, dicionario.tempo, dicionario.velocidade, dicionario.consumo, dicionario.aceleracao, dicionario.x, dicionario.y, dicionario.rpm)


    fig, ax = plt.subplots(2,2)
    
     
    #TRATAMENTO DE VELOCIDADE
    ax.plot(tabela["tempo"], tabela["velocidade"], 'o-', color='#ff7f0e', label='Velocidade')
    ax.title('Velocidade do Carro em Função do Tempo')
    ax.xlabel('Tempo (s)')
    ax.ylabel('Velocidade (m/s)')
    ax.legend()
    ax.xticks(x)
    ax.yticks(y)
    ax.grid()

    












#dados permanentes - calculados só no final da corrida


