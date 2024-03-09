import random

dicionario = {"volta": [], "tempo": [], "velocidade": [], "consumo": [], "aceleracao": [], "x": [], "y": [], "rpm": []}

def chegada_dados_prontos(i):
    voltamock = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    tempomock = [1, 2, 3, 4, 5,6 ,7 ,8, 9, 10]
    velocidademock = [12, 14, 20, 16, 14, 16, 18, 12, 13, 16]
    consumomock =  [100000, 13877, 19273, 19272, 138713, 34564, 77645, 8876, 8747, 76545]
    aceleracaomock = [2, 3, 1, 4, 5, 9, 6, 5, 4, 4]
    xmock = [2377943, 38923932, 3293289, 2389238, 233232, 92728, 3682, 928273, 82873, 82737]
    ymock = [93393, 2392039, 32328, 238328, 32982, 273728, 923873, 928327, 93827, 938273]
    rpmmock = [100, 21, 2121, 2123, 3232, 2323, 2323, 444, 555, 666]

    dicionario["volta"] = voltamock[i]
    dicionario["tempo"] = tempomock[i]
    dicionario["velocidade"] = velocidademock[i]
    dicionario["consumo"] = consumomock[i]
    dicionario["aceleracao"] = aceleracaomock[i]
    dicionario["x"] = xmock[i]
    dicionario["y"] = ymock[i]
    dicionario["rpm"] = rpmmock[i]
    return dicionario

def chegada_dados():
    velocidade = random.randint(10,15)
    return velocidade

