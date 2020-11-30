"""
    Arquivo que possibililita a conexão com o Banco de dados Mysql
"""
# Imports
from mysql.connector import connect


config = {
    'user': 'usuario_mysql',
    'password': 'senha_mysql',
    'host': '100.000.00.00',
    'database': 'banco_de_dados',
    'raise_on_warnings': True   # feedback da conexão
}

connection = connect(**config)