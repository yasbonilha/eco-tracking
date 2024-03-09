import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
from mock.mock_leitura_dados import chegada_dados_prontos

#dados instantâneos
tabela = pd.DataFrame(columns = ["volta", "tempo", "velocidade", "consumo", "aceleracao", "x", "y", "rpm"])


def tratar_dados_instantaneos():
    global tabela

    plt.ion()

    for i in range(10):
        tabela = pd.concat([tabela, pd.DataFrame([chegada_dados_prontos(i)])])
        print(tabela)
        plt.plot(tabela["tempo"], tabela["velocidade"], 'o-', label='Velocidade')
        plt.title('Velocidade do Carro em Função do Tempo')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Velocidade (m/s)')
        plt.legend()
        plt.xticks(range(0,60,3))
        plt.yticks(range(0,50, 10))
        plt.grid()
        plt.show()
        plt.pause(1)
        plt.cla()
        plt.clf()

    plt.ioff()

    return tabela
# color='#ff7f0e',
    












#dados permanentes - calculados só no final da corrida


