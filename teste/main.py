from config import db_config
import mysql.connector

conexao = None

try:
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50) NOT NULL,
            preco DECIMAL(10,2) NOT NULL,
            quantidade INT NOT NULL,
            categoria VARCHAR(50) NOT NULL
        )
    """)

    conexao.commit()
    print("Tabela criada com sucesso!")

except mysql.connector.Error as erro:
    print("Erro:", erro)

finally:
    if conexao and conexao.is_connected():
        conexao.close()