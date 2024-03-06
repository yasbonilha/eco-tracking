import mysql.connector

def conexao_bd():
    try:
        # Conecta ao banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Cizy@3008",
            database="ecotracking")

        print("conexão com banco de dados feita com sucesso!")
        return conexao

    except mysql.connector.Error as erro:
        print("Erro ao acessar a base de dados:", erro)