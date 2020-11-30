# Imports de modolus internos da aplicação
from infra.equivalente_concorrente.equivalente_concorrente_dao import \
    listar as dao_listar, \
    cadastrar as dao_cadastrar, \
    consultar as dao_consultar_id, \
    remover as dao_remover

from model.equivalente_concorrente import Equivalente_concorrente


# Função que lista conteudo
def listar():
    return [equivalente_concorrente for equivalente_concorrente in dao_listar()]


# Função que localiza concorrente por ID
def localizar(id):
    equivalente_concorrente = dao_consultar_id(id)
    if equivalente_concorrente is None:
        return None
    return equivalente_concorrente


# Função que cria Usuario
def criar(equivalente_concorrente):
    equivalente = Equivalente_concorrente.criar(equivalente_concorrente)
    return dao_cadastrar(equivalente)


# Função que remove concorrente
def remover(deletavel):
    dados_equivalente_concorrente = deletavel
    if dados_equivalente_concorrente is None:
        return 0
    dao_remover(dados_equivalente_concorrente)
    return 1
