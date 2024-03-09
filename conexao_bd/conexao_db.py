import mysql.connector
from sqlalchemy import create_engine


def conexao_bd():
    try:
        # Conecta ao banco de dados
        conexao = mysql.connector.connect(
            host="localhost",
            user="yasmin",
            password="Yasmin2005",
            database="ecotracking")
        
        engine = create_engine("mysql+mysqlconnector://yasmin:Yasmin2005@localhost/ecotracking")

        print("conexão com banco de dados feita com sucesso!")
        return conexao, engine

    except mysql.connector.Error as erro:
        print("Erro ao acessar a base de dados:", erro)