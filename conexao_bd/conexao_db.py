import mysql.connector
from sqlalchemy import create_engine

'''
pagina destinada a fazer a conexao com o banco de dados. criamos a conexao com o nome do usuario, senha, nome do banco de dados e o host (que geralmente e localhost). criamos a engine para poder passar direto do dataframe para o banco de dados.
'''
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