# Class que representa o modelo no banco
class Equivalente_concorrente:

    def __init__(self, id_concorrente, id_produto):
        self.id_concorrente = id_concorrente
        self.id_produto = id_produto

    def atualizar(self, dados):
        try:
            id_concorrente = dados["id_concorrente"]
            id_produto = dados["id_produto"]
            self.id_concorrente, self.id_produto = id_concorrente, id_produto
            return self
        except Exception as e:
            print("Problema ao criar novo Usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d['id_concorrente'] = self.id_concorrente
        d['id_produto'] = self.id_produto
        return d

    @staticmethod
    def criar(dados):
        try:
            id_concorrente = dados["id_concorrente"]
            id_produto = dados["id_produto"]
            return Equivalente_concorrente(id_concorrente=id_concorrente, id_produto=id_produto)
        except Exception as e:
            print("Problema ao criar novo Equivalente_concorrente!")
            print(e)
