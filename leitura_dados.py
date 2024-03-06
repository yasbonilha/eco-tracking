import serial

# Configura a comunicação serial com o Arduino
arduino = serial.Serial('COM7', 9600)  

# Aguarda a inicialização do Arduino
arduino.readline()

# Lê os dados enviados pelo Arduino e faz um "pacotinho" para o tratamento
def ler_dados():
# Lê uma linha da porta serial
    dados = arduino.readline().decode().strip()

    # Separa os dados em uma lista
    valores = dados.split(',')

    # Se a lista tiver 6 valores (correspondendo às 6 colunas), adiciona-os ao banco de dados
    if len(valores) == 8:
        volta, tempo, velocidade, consumo, aceleracao, x, y, rpm = map(float, valores)
        dados = {"volta": volta, "tempo": tempo, "velocidade": velocidade, "consumo": consumo,  "aceleracao": aceleracao, "x": x, "y": y, "rpm": rpm}
        return dados

    
    
