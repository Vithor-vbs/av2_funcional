from flask import Flask, request, jsonify
from passlib.hash import sha256_crypt

app = Flask(__name__)

class ContaBancaria:
    def __init__(self, senha, saldo):
        self.senha = sha256_crypt.hash(senha)  # Armazenar a senha criptografada
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, nome, senha, saldo):
        self.usuarios[nome] = ContaBancaria(senha, saldo)

    def login(self, nome, senha):
        return (lambda nome, senha: nome in self.usuarios and self.usuarios[nome].senha == senha)(nome, senha)

    def verificar_saldo_suficiente(self, nome, valor):
        return (lambda nome, valor: nome in self.usuarios and self.usuarios[nome].saldo >= valor)(nome, valor)

    def descontar_saldo(self, nome, valor):
        (lambda nome, valor: setattr(self.usuarios[nome], "saldo", self.usuarios[nome].saldo - valor))(nome, valor)

    def creditar_saldo(self, nome, valor):
        (lambda nome, valor: setattr(self.usuarios[nome], "saldo", self.usuarios[nome].saldo + valor))(nome, valor)

class OperacoesBancarias:
    def __init__(self, banco):
        self.banco = banco
    
    def get_user_balance(self, nome):
        return self.banco.usuarios[nome].saldo if nome in self.banco.usuarios else None

    def cash(self, nome, valor):
        if self.banco.verificar_saldo_suficiente(nome, valor):
            self.banco.descontar_saldo(nome, valor)
            return f"Pagamento de R$ {valor} efetuado com sucesso.\nSaldo atual: {self.get_user_balance(nome)}"
        else:
            return f"Saldo insuficiente para efetuar o pagamento de R$ {valor}."

    def fund(self, nome_origem, nome_destino, valor):
        if nome_destino in self.banco.usuarios and self.banco.verificar_saldo_suficiente(nome_origem, valor):
            self.banco.descontar_saldo(nome_origem, valor)
            self.banco.creditar_saldo(nome_destino, valor)
            return f"Transferência de R$ {valor} para a conta {nome_destino} efetuada com sucesso.\nSaldo atual: {self.get_user_balance(nome_destino)}"
        else:
            return "Conta inválida ou saldo insuficiente."

    def credit(self, nome_destino, valor):
        if nome_destino in self.banco.usuarios:
            self.banco.creditar_saldo(nome_destino, valor)
            return f"Crédito de R$ {valor} na conta {nome_destino} efetuado com sucesso.\nSaldo atual: {self.get_user_balance(nome_destino)}"
        else:
            return "Conta inválida."

# Criar instância do banco e das operações bancárias
banco = Banco()
banco.adicionar_usuario("usuario1", "1234", 1000)
banco.adicionar_usuario("usuario2", "5678", 2000)
operacoes = OperacoesBancarias(banco)

# Rotas Flask
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    nome = data.get('nome')
    senha = data.get('senha')
    if nome and senha:
        if banco.login(nome, senha):
            return jsonify({"mensagem": "Login bem-sucedido"})
    return jsonify({"mensagem": "Credenciais inválidas"}), 401

@app.route('/cash', methods=['POST'])
def cash():
    data = request.get_json()
    nome = data.get('nome')
    valor = data.get('valor')
    if nome and valor:
        return operacoes.cash(nome, valor)
    return jsonify({"mensagem": "Dados inválidos"}), 400

@app.route('/fund', methods=['POST'])
def fund():
    data = request.get_json()
    nome_origem = data.get('nome_origem')
    nome_destino = data.get('nome_destino')
    valor = data.get('valor')
    if nome_origem and nome_destino and valor:
        return operacoes.fund(nome_origem, nome_destino, valor)
    return jsonify({"mensagem": "Dados inválidos"}), 400

@app.route('/credit', methods=['POST'])
def credit():
    data = request.get_json()
    nome_destino = data.get('nome_destino')
    valor = data.get('valor')
    if nome_destino and valor:
        return operacoes.credit(nome_destino, valor)
    return jsonify({"mensagem": "Dados inválidos"}), 400

if __name__ == '__main__':
    app.run(debug=True)