# Imports de modolus internos da aplicação
from infra.concorrente.concorrente_dao import \
    listar as dao_listar_concorrente, \
    consultar as dao_consultar_id, \
    cadastrar as dao_cadastrar_concorrente, \
    alterar as dao_alterar_concorrente, \
    remover as dao_remover_concorrente, \
    consultar_concorrente as dao_consultar_concorrente
from model.concorrente import Concorrente


# Função que lista concorrente
def listar():
    return [concorrente for concorrente in dao_listar_concorrente()]


# Função que localiza concorrente por ID
def localizar(id):
    concorrente = dao_consultar_id(id)
    if concorrente is None:
        return None
    return concorrente


# Função que localiza concorrente por ID
def localizar_concorrente(concorrente):
    concorrente = dao_consultar_concorrente(concorrente)
    if concorrente is None:
        return None
    return concorrente


# Função que cria concorrente
def criar(concorrente_dados):
    concorrente = Concorrente.criar(concorrente_dados)
    return dao_cadastrar_concorrente(concorrente)


# Função que remove concorrente
def remover(id):
    dados_concorrente = localizar(id)
    if dados_concorrente is None:
        return 0
    dao_remover_concorrente(dados_concorrente)
    return 1


# Função que atualiza concorrente
def atualizar(id, codigo_concorrente, descricao_concorrente,
              empresa_concorrente, observacao_concorrente):
    concorrente = {"codigo_concorrente": codigo_concorrente, "descricao_concorrente": descricao_concorrente,
                   "empresa_concorrente": empresa_concorrente, "observacao_concorrente": observacao_concorrente,
                   "id": id}

    dao_alterar_concorrente(concorrente)
    return localizar(id)
