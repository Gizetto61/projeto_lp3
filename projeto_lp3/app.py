from flask import Flask, render_template
from validate_docbr import CPF
from validate_docbr import CNPJ

app = Flask(__name__)


# rota + função

@app.route("/termos")
def Termos():
    return render_template("termos.html")

@app.route("/politica")
def Politica():
    return render_template("politica.html")

@app.route("/ultilizacao")
def Ultilizacao():
    return render_template("ultilizacao.html")

# / = home page
@app.route("/")
def home():
    return render_template("home.html")

# /contato = página de contato
@app.route("/contato")
def contato():
    return render_template("contato.html")

# /produtos = pagina produtos
@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome": "Coca-cola", "descricao": "Mata a sede", "imagem": "https://www.callfarma.com.br/_next/image?url=https%3A%2F%2Fd2lakedouw4zad.cloudfront.net%2Fcoca-cola-lata-350ml-74082.png&w=828&q=75"},
        {"nome": "Doritos", "descricao": "Suja a mão", "imagem": "https://http2.mlstatic.com/D_628495-MLB75957680171_042024-C.jpg"},
        {"nome": "Red Bull", "descricao": "Te dá Asas", "imagem": "https://d1w7bbx0g2e0q3.cloudfront.net/redbull/products/tmp_JJwqkjWCSUzTgico.png"},
    ]
    return render_template("produtos.html", produtos = lista_produtos)

# página /servicos retorna "Nossos Serviços"
# página /gerar-cpf retornar um cpf aleatório
# página /gerar-cnpj retornar cnpj aleatório

# /serviços = pagina serviços
@app.route("/servicos")
def servicos():
    return "<h1>Nossos Serviços</h1>"

@app.route("/gerar-cpf")
def gerarcpf():
    cpf = CPF()
    lista = {cpf.generate(True)}
    return render_template("CPF.html", cpf = lista)

@app.route("/gerar-cnpj")
def gerarcnpj():
    cnpj = CNPJ()
    lista1 = {cnpj.generate(True)}
    return render_template("CNPJ.html", cnpj = lista1)

app.run()