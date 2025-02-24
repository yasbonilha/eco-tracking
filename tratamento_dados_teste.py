import pandas as pd
# APLICACAO FLASK: o use Agg roda o plt em "segundo plano", mas não roda GUI - então ele não mostra os gráficos
# import matplotlib
# matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from mock.mock_leitura_dados import chegada_dados_prontos, chegada_dados, chegada_dados_csv
import numpy as np

'''
pagina destinada a receber os dados do arduino e trata-los. na funcao instantanea, criamos um df e plotamos um grafico com base nele, que e atualizado de forma recorrente, e devolve o proprio df. funcao permanente ainda a ser terminada.
'''
#dados instantâneos
tabela = pd.DataFrame(columns = ["aceleracao", "latitude", "longitude", "tempo", "tensao", "corrente", "consumo", "rpm", "velocidade", "volta"])

fig, axs = plt.subplots(1, 2, figsize=(12, 6))  # criação de duas subtramas

for ax in axs:
    ax.grid()


def tratar_dados_instantaneos():
    global tabela

    plt.ion()

    for i in range(20):
        print(tabela)
        tabela = pd.concat([tabela, pd.DataFrame([chegada_dados_csv(i)])])
        print(tabela)
        # Plotagem no primeiro gráfico
        axs[0].plot(tabela["tempo"], tabela["velocidade"], 'o-', color='blue')  # Alteração de cor para azul
        axs[0].set_title('Velocidade do Carro em Função do Tempo')
        
        axs[0].set_xlabel('Tempo (s)')
        axs[0].set_ylabel('Velocidade (m/s)')
        axs[0].legend(['Velocidade'])  # Apenas um rótulo para a legenda
        axs[0].set_xticks(range(0, 40, 5))
        axs[0].set_yticks(range(0, 50, 10))

        # Plotagem no segundo gráfico
        axs[1].plot(tabela["tempo"], tabela["consumo"], 'o-', color='orange', label='Consumo')
        axs[1].set_title('Consumo do Carro em Função do Tempo')
        axs[1].set_xlabel('Tempo (s)')
        axs[1].set_ylabel('Consumo (L)')
        axs[1].legend()
        axs[1].set_xticks(range(0, 40, 5))
        axs[1].set_yticks(range(0, 4000, 1000))
        axs[1].grid()

        plt.pause(1)
        plt.cla()

    plt.ioff()
    
    
    print("Dados instantâneos tratados com sucesso.")
    lista_tabela = [row.tolist() for index, row in tabela.iterrows()]
    return lista_tabela