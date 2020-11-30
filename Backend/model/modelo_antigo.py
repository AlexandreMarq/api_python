# Class que representa o modelo no bancoclass Manual:

class Modelo_antigo:
    def __init__(self, descricao_modelo_antigo, modelo_antigo,
                 observacao_modelo_antigo, id_foto):
        self.descricao_modelo_antigo = descricao_modelo_antigo
        self.modelo_antigo = modelo_antigo
        self.observacao_modelo_antigo = observacao_modelo_antigo
        self.id_foto = id_foto

    def atualizar(self, dados):
        try:
            descricao_modelo_antigo = dados["descricao_modelo_antigo"]
            modelo_antigo = dados["modelo_antigo"]
            observacao_modelo_antigo = dados["observacao_modelo_antigo"]
            id_foto = dados["id_foto"]

            self.descricao_modelo_antigo = descricao_modelo_antigo,
            self.modelo_antigo = modelo_antigo,
            self.observacao_modelo_antigo = observacao_modelo_antigo,
            self.id_foto = id_foto
            return self
        except Exception as e:
            print("Problema ao criar novo Concorrente!")
            print(e)

    def __dict__(self):
        d = dict()
        d['descricao_modelo_antigo'] = self.descricao_modelo_antigo
        d['modelo_antigo'] = self.modelo_antigo
        d['observacao_modelo_antigo'] = self.observacao_modelo_antigo
        d['id_foto'] = self.id_foto
        return d

    @staticmethod
    def criar(dados):
        try:
            descricao_modelo_antigo = dados["descricao_modelo_antigo"]
            modelo_antigo = dados["modelo_antigo"]
            observacao_modelo_antigo = dados["observacao_modelo_antigo"]
            id_foto = dados["id_foto"]
            return Modelo_antigo(descricao_modelo_antigo=descricao_modelo_antigo,
                                 modelo_antigo=modelo_antigo,
                                 observacao_modelo_antigo=observacao_modelo_antigo,
                                 id_foto=id_foto)
        except Exception as e:
            print("Problema ao criar novo Concorrente!")
            print(e)
