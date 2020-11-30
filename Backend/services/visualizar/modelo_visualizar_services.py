# Imports de modolus internos
from infra.visualizar.modelo_antigo_vizualizar_dao import consultar


# Função que localiza produto por ID
def localizar_modelo(id):
    modelo = consultar(id)
    if modelo is None:
        return None
    return modelo

