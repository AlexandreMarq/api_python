# Imports de modolus internos
from infra.visualizar.concorrente_visualizar_dao import consultar


# Função que localiza produto por ID
def localizar_concorente(id):
    concorente = consultar(id)
    if concorente is None:
        return None
    return concorente

