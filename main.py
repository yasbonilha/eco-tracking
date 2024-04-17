from flask import Flask, render_template
from tratamento_dados_teste import tratar_dados_instantaneos

app = Flask(__name__)

@app.route('/')
def home():
    tabela = tratar_dados_instantaneos()
    return tabela

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

if __name__ == '__main__':
    app.run(debug=True)
