import mysql.connector
from conexao_bd.conexao_db import conexao_bd

#pega os dados tratados do dataframe e insere eles na tabela ao final da corrida
def inserir_dados(volta, tempo, velocidade, vm, consumo, aceleracao, x, y, rpm):
    try:

        conexao = conexao_bd()
        
        # Cria um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Comando SQL para inserir dados na tabela
        comando_sql = "INSERT INTO ecoTreino (volta, tempo, velocidade, vm, consumo, aceleracao, x, y, rpm) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        
        # Executa o comando SQL passando os valores como parâmetros
        cursor.execute(comando_sql, (volta, tempo, velocidade, vm, consumo, aceleracao, x, y, rpm))

        # Comita a transação
        conexao.commit()

        print("Dados adicionados com sucesso!")

    except mysql.connector.Error as erro:
        print("Erro ao adicionar dados:", erro)

    finally:
        # Fecha a conexão com o banco de dados
        if conexao.is_connected():
            cursor.close()
            conexao.close()
