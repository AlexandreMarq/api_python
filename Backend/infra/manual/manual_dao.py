# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "manual"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_manual, link_manual, manual_idioma, manual_tipo, nome_manual) in rows:
        registros.append(
            {"id_manual": id_manual, "link_manual": link_manual, "manual_idioma": manual_idioma,
                "manual_tipo": manual_tipo, "nome_manual": nome_manual})
    
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_manual = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    
    cursor.close()
    return ({"id_manual": row[0], "link_manual": row[1], "manual_idioma": row[2],
                "manual_tipo": row[3], "nome_manual": row[4]})
