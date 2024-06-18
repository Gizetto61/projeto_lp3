from flask import Flask, render_template
from validate_docbr import CPF
from validate_docbr import CNPJ

app = Flask(__name__)


# rota + função

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
        {"nome": "Coca-cola", "descricao": "Mata a sede"},
        {"nome": "Doritos", "descricao": "Suja a mão"},
        {"nome": "Red Bull", "descricao": "Te dá Asas"},
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
    return cpf.generate(True)

@app.route("/gerar-cnpj")
def gerarcnpj():
    cnpj = CNPJ()
    return cnpj.generate(True)

app.run()