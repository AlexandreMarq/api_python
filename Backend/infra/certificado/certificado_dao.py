# Imports
from mysql.connector import connect
from BD.banco import connection

# Tabela
model_name = "certificado"


# Query que lista tudo da tabela
def listar():
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {model_name};")
    rows = cursor.fetchall()
    registros = []
    for (id_certificado, certificado) in rows:
        registros.append(
            {"id_certificado": id_certificado, "certificado": certificado})
   
    cursor.close()
    return registros


# Query que consulta por ID a tabela
def consultar(id):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT * FROM {model_name} WHERE id_certificado = %s", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    
    cursor.close()
    return ({"id_certificado": row[0], "certificado": row[1]})
