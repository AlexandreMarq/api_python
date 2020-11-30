# Imports
from mysql.connector import connect
from BD.banco import connection


# Tabela
model_name = "aplicacao"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_aplicacao, aplicacao) in rows:
        registros.append(
            {"id_aplicacao": id_aplicacao, "aplicacao": aplicacao})
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_aplicacao = %s;", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    cursor.close()
    return ({"id_aplicacao": row[0], "aplicacao": row[1]})