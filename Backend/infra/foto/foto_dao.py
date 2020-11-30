# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "foto"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_foto, link_foto, nome_foto) in rows:
        registros.append(
            {"id_foto": id_foto, "link_foto": link_foto, "nome_foto": nome_foto})

    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_foto = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    
    cursor.close()
    return ({"id_foto": row[0], "foto": row[1]})
