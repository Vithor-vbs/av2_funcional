class ContaBancaria:
    def __init__(self, senha, saldo):
        self.senha = senha
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
        return (lambda nome: self.banco.usuarios[nome].saldo)(nome)

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

# Criar instâncias do banco e das operações bancárias
banco = Banco()
banco.adicionar_usuario("usuario1", 1234, 1000)
banco.adicionar_usuario("usuario2", 5678, 2000)
operacoes = OperacoesBancarias(banco)

# Exemplo de uso
print(banco.login("usuario1", 1234))  
print(operacoes.cash("usuario1", 500)) 
print(operacoes.fund("usuario1", "usuario2", 300))  
print(operacoes.credit("usuario2", 200)) 
