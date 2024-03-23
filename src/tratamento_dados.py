import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
from mock.mock_leitura_dados import chegada_dados_prontos, chegada_dados
import numpy as np

'''
pagina destinada a receber os dados do arduino e trata-los. na funcao instantanea, criamos um df e plotamos um grafico com base nele, que e atualizado de forma recorrente, e devolve o proprio df. funcao permanente ainda a ser terminada.
'''
#dados instantâneos
tabela = pd.DataFrame(columns = ["volta", "tempo", "velocidade", "consumo", "aceleracao", "x", "y", "rpm"])


def tratar_dados_instantaneos():
    global tabela

    plt.ion()

    for i in range(20):
        tabela = pd.concat([tabela, pd.DataFrame([chegada_dados(i)])])
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
    plt.show()




    print("dados instantâneos tratados com sucesso.")
    return tabela
    
def tratar_dados_permanentes():
    vm = tabela["velocidade"].mean()
    mrpm = tabela["rpm"].mean()
    mtempovolta = tabela.groupby(["volta"], as_index=False)["tempo"].mean()
    print("dados permanentes tratados com sucesso.")


