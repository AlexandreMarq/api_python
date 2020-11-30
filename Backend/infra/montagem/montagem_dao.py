# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "montagem"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_montagem, montagem) in rows:
        registros.append(
            {"id_montagem": id_montagem,
             "montagem": montagem})
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_montagem = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    cursor.close()
    return ({"id_montagem": row[0], "montagem": row[1]})
