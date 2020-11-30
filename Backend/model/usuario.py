# Class que representa o modelo no bancoclass Manual:

class Usuario:

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def atualizar(self, dados):
        try:
            login = dados["login"]
            senha = dados["senha"]
            self.login, self.senha = login, senha
            return self
        except Exception as e:
            print("Problema ao criar novo Usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d['login'] = self.login
        d['senha'] = self.senha
        return d

    @staticmethod
    def criar(dados):
        try:
            login = dados["login"]
            senha = dados["senha"]
            return Usuario(login=login, senha=senha)
        except Exception as e:
            print("Problema ao criar novo Usuario!")
            print(e)
