# Imports de modolus internos da aplicação
from infra.equivalente_antigo.equivalente_antigo_dao import \
    listar as dao_listar, \
    cadastrar as dao_cadastrar, \
    consultar as dao_consultar_id, \
    remover as dao_remover

from model.equivalente_antigo import Equivalente_antigo


# Função que lista conteudo
def listar():
    return [equivalente_antigo for equivalente_antigo in dao_listar()]


# Função que localiza concorrente por ID
def localizar(id):
    equivalente_antigo = dao_consultar_id(id)
    if equivalente_antigo is None:
        return None
    return equivalente_antigo


# Função que cria Usuario
def criar(equivalente_antigo):
    equivalente = Equivalente_antigo.criar(equivalente_antigo)
    return dao_cadastrar(equivalente)


# Função que remove concorrente
def remover(deletavel):
    dados_equivalente_antigo = deletavel
    if dados_equivalente_antigo is None:
        return 0
    dao_remover(dados_equivalente_antigo)
    return 1