from flask import Flask
from validate_docbr import CPF
from validate_docbr import CNPJ

app = Flask(__name__)


# rota + função

# / = home page
@app.route("/")
def home():
    return "<h1>Home Page</h1>"

# /contato = página de contato
@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

# /produtos = pagina produtos
@app.route("/produtos")
def produtos():
    return "<h1>Produtos</h1>"

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