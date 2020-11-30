# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "alimentacao"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_alimentacao, alimentacao) in rows:
        registros.append(
            {"id_alimentacao": id_alimentacao, "alimentacao": alimentacao})
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_alimentacao = %s;", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    cursor.close()
    return ({"id_alimentacao": row[0], "alimentacao": row[1]})