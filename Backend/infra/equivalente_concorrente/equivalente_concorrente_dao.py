# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "equivalente_concorrente"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_equivalente_concorrente, id_concorrente, id_produto) in rows:
        registros.append(
            {"id_equivalente_concorrente": id_equivalente_concorrente,
             "id_concorrente": id_concorrente,
             "id_produto": id_produto})
    
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_equivalente_concorrente = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    
    cursor.close()
    return ({"id_equivalente_concorrente": row[0],
             "id_concorrente": row[1],
             "id_produto": row[2]})


# Query que insere os dados na tabela
def cadastrar(equivalente_concorrente):
    cursor = connection.cursor()
    sql = f"INSERT INTO {model_name} (id_concorrente, id_produto) VALUES (%s, %s)"
    cursor.execute(sql, (equivalente_concorrente.id_concorrente, equivalente_concorrente.id_produto))
    
    cursor.close()
    connection.commit()

    return equivalente_concorrente.__dict__()


# Query que remove os dados na tabela
def remover(deletavel):
    cursor = connection.cursor()
    sql = f"DELETE FROM {model_name} WHERE id_equivalente_concorrente in ({deletavel})"
    cursor.execute(sql)

    cursor.close()
    connection.commit()

