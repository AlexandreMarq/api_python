# Imports de modolus internos da aplicação
from infra.certificado.certificado_dao import \
    listar as dao_listar, \
    consultar as dao_consultar


# Função que lista Certificado
def listar():
    return [certificado for certificado in dao_listar()]


# Função que localiza Certificado por ID
def localizar(id):
    certificado = dao_consultar(id)
    if certificado is None:
        return None
    return certificado
