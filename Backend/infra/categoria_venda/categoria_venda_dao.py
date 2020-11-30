# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "categoria_venda"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_categoria, categoria_venda) in rows:
        registros.append(
            {"id_categoria": id_categoria, "categoria_venda": categoria_venda})

    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_categoria = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    cursor.close()
    return ({"id_categoria": row[0], "categoria_venda": row[1]})
