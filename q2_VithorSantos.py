from q1_VithorSantos import *

import unittest

class TestOperacoesBancarias(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()
        self.banco.adicionar_usuario("usuario1", 1234, 1000)
        self.banco.adicionar_usuario("usuario2", 5678, 2000)
        self.operacoes = OperacoesBancarias(self.banco)

    def test_cash_com_saldo_suficiente(self):
        test_cash = lambda usuario, valor: (
            self.operacoes.cash(usuario, valor),
            f"Pagamento de R$ {valor} efetuado com sucesso.\nSaldo atual: {valor}"
        )
        resultado, resultado_esperado = test_cash("usuario1", 500)
        self.assertEqual(resultado, resultado_esperado)

    def test_cash_com_saldo_insuficiente(self):
        test_cash = lambda usuario, valor: (
            self.operacoes.cash(usuario, valor),
            "Saldo insuficiente para efetuar o pagamento de R$ 1500."
        )
        resultado, resultado_esperado = test_cash("usuario1", 1500)
        self.assertEqual(resultado, resultado_esperado)

    def test_fund_com_saldo_suficiente(self):
        test_fund = lambda usuario_origem, usuario_destino, valor: (
            self.operacoes.fund(usuario_origem, usuario_destino, valor),
            f"Transferência de R$ {valor} para a conta {usuario_destino} efetuada com sucesso.\nSaldo atual: {self.operacoes.get_user_balance(usuario_destino)}"
        )
        resultado, resultado_esperado = test_fund("usuario1", "usuario2", 300)
        self.assertEqual(resultado, resultado_esperado)

    def test_fund_com_saldo_insuficiente(self):
        test_fund = lambda usuario_origem, usuario_destino, valor: (
            self.operacoes.fund(usuario_origem, usuario_destino, valor),
            "Conta inválida ou saldo insuficiente."
        )
        resultado, resultado_esperado = test_fund("usuario1", "usuario2", 2000)
        self.assertEqual(resultado, resultado_esperado)

class TestOperacoesBancariasStress(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()
        self.banco.adicionar_usuario("usuario1", 1234, 1000000)
        self.banco.adicionar_usuario("usuario2", 5678, 1000000)
        self.operacoes = OperacoesBancarias(self.banco)

    def test_stress_cash(self):
        for _ in range(10000):
            resultado = self.operacoes.cash("usuario1", 100)
            self.assertTrue("efetuado com sucesso" in resultado)
    
    def test_stress_fund(self):
        for _ in range(10000):
            resultado = self.operacoes.fund("usuario1", "usuario2", 100)
            self.assertTrue("efetuada com sucesso" in resultado)

if __name__ == '__main__':
    unittest.main()

# rodando testes:
# $ python -m unittest q2_VithorSantos.py 