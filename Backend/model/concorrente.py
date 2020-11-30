# Class que representa o modelo no banco
class Concorrente:
    def __init__(self, codigo_concorrente, descricao_concorrente,
                 empresa_concorrente, observacao_concorrente):
        self.codigo_concorrente = codigo_concorrente
        self.descricao_concorrente = descricao_concorrente
        self.empresa_concorrente = empresa_concorrente
        self.observacao_concorrente = observacao_concorrente

    def atualizar(self, dados):
        try:
            codigo_concorrente = dados["codigo_concorrente"]
            descricao_concorrente = dados["descricao_concorrente"]
            empresa_concorrente = dados["empresa_concorrente"]
            observacao_concorrente = dados["observacao_concorrente"]

            self.codigo_concorrente = codigo_concorrente,
            self.descricao_concorrente = descricao_concorrente,
            self.empresa_concorrente = empresa_concorrente,
            self.observacao_concorrente = observacao_concorrente
            return self
        except Exception as e:
            print("Problema ao criar novo Concorrente!")
            print(e)

    def __dict__(self):
        d = dict()
        d['codigo_concorrente'] = self.codigo_concorrente
        d['descricao_concorrente'] = self.descricao_concorrente
        d['empresa_concorrente'] = self.empresa_concorrente
        d['observacao_concorrente'] = self.observacao_concorrente
        return d

    @staticmethod
    def criar(dados):
        try:
            codigo_concorrente = dados["codigo_concorrente"]
            descricao_concorrente = dados["descricao_concorrente"]
            empresa_concorrente = dados["empresa_concorrente"]
            observacao_concorrente = dados["observacao_concorrente"]
            return Concorrente(codigo_concorrente=codigo_concorrente,
                               descricao_concorrente=descricao_concorrente,
                               empresa_concorrente=empresa_concorrente,
                               observacao_concorrente=observacao_concorrente)
        except Exception as e:
            print("Problema ao criar novo Concorrente!")
            print(e)
