# Imports
from mysql.connector import connect
from BD.banco import connection


# Tabela
model_name = "aplicacao_navegacao"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_aplicacao_navegacao, aplicacao_navegacao) in rows:
        registros.append(
            {"id_aplicacao_navegacao": id_aplicacao_navegacao,
             "aplicacao_navegacao": aplicacao_navegacao})
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_aplicacao_navegacao = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    cursor.close()
    return ({"id_aplicacao_navegacao": row[0], "aplicacao_navegacao": row[1]})
