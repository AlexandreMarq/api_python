# Class que representa o modelo no banco
class Equivalente_antigo:

    def __init__(self, id_modelo_antigo, id_produto):
        self.id_modelo_antigo = id_modelo_antigo
        self.id_produto = id_produto

    def atualizar(self, dados):
        try:
            id_modelo_antigo = dados["id_modelo_antigo"]
            id_produto = dados["id_produto"]
            self.id_modelo_antigo, self.id_produto = id_modelo_antigo, id_produto
            return self
        except Exception as e:
            print("Problema ao criar novo Usuario!")
            print(e)

    def __dict__(self):
        d = dict()
        d['id_modelo_antigo'] = self.id_modelo_antigo
        d['id_produto'] = self.id_produto
        return d

    @staticmethod
    def criar(dados):
        try:
            id_modelo_antigo = dados["id_modelo_antigo"]
            id_produto = dados["id_produto"]
            return Equivalente_antigo(id_modelo_antigo=id_modelo_antigo, id_produto=id_produto)
        except Exception as e:
            print("Problema ao criar novo Equivalente_antigo!")
            print(e)
