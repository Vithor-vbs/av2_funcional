import json
import unittest
import requests

class TestApp(unittest.TestCase):
    def setUp(self):
        self.url_login = 'http://127.0.0.1:5000/login'
        self.url_cash = 'http://127.0.0.1:5000/cash'
        self.url_fund = 'http://127.0.0.1:5000/fund'
        self.url_credit = 'http://127.0.0.1:5000/credit'

    # def test_login(self):
    #     data = {"nome": "usuario1", "senha": "1234"}
    #     response = requests.post(self.url_login, json=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("Login bem-sucedido", response.json()["mensagem"])

    def test_cash(self):
        data = {"nome": "usuario1", "valor": 500}
        response = requests.post(self.url_cash, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Pagamento de R$ 500 efetuado com sucesso", response.json()["mensagem"])

    # def test_fund(self):
    #     data = {"nome_origem": "usuario1", "nome_destino": "usuario2", "valor": 300}
    #     response = requests.post(self.url_fund, json=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("Transferência de R$ 300 para a conta usuario2 efetuada com sucesso", response.json()["mensagem"])

    # def test_credit(self):
    #     data = {"nome_destino": "usuario2", "valor": 200}
    #     response = requests.post(self.url_credit, json=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("Crédito de R$ 200 na conta usuario2 efetuado com sucesso", response.json()["mensagem"])

if __name__ == '__main__':
    unittest.main()