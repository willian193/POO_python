import mysql.connector
from config import db_config

def criar_tabela():
    conexao = None
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                telefone VARCHAR(20)
            )
        """)
        conexao.commit()
        print("Tabela 'cliente' verificada/criada com sucesso!")

    except mysql.connector.Error as erro:
        print("Erro ao criar tabela:", erro)

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def cadastrar_cliente():
    nome = input("Digite o nome: ").strip()
    email = input("Digite o e-mail: ").strip()
    telefone = input("Digite o telefone: ").strip()

    conexao = None
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = "INSERT INTO cliente (nome, email, telefone) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, telefone))
        conexao.commit()

        print(f"Cliente '{nome}' cadastrado com sucesso!")

    except mysql.connector.Error as erro:
        print("Erro ao cadastrar cliente:", erro)

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def listar_clientes():
    conexao = None
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome, email, telefone FROM cliente")
        clientes = cursor.fetchall()

        print("\n--- LISTA DE CLIENTES ---")
        if clientes:
            for c in clientes:
                print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]} | Telefone: {c[3]}")
        else:
            print("Nenhum cliente cadastrado.")

    except mysql.connector.Error as erro:
        print("Erro ao listar clientes:", erro)

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def buscar_cliente():
    termo = input("Digite o nome (ou parte dele) para buscar: ").strip()

    conexao = None
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = "SELECT id, nome, email, telefone FROM cliente WHERE nome LIKE %s"
        cursor.execute(sql, (f"%{termo}%",))
        resultados = cursor.fetchall()

        print("\n--- RESULTADO DA BUSCA ---")
        if resultados:
            for c in resultados:
                print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]} | Telefone: {c[3]}")
        else:
            print("Nenhum cliente encontrado com esse nome.")

    except mysql.connector.Error as erro:
        print("Erro ao buscar cliente:", erro)

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def atualizar_email():
    try:
        id_cliente = int(input("Digite o ID do cliente: "))
        novo_email = input("Digite o novo e-mail: ").strip()
    except ValueError:
        print("ID inválido! Digite apenas números.")
        return

    conexao = None
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = "UPDATE cliente SET email = %s WHERE id = %s"
        cursor.execute(sql, (novo_email, id_cliente))
        conexao.commit()

        if cursor.rowcount > 0:
            print("E-mail atualizado com sucesso!")
        else:
            print("Nenhum cliente encontrado com esse ID.")

    except mysql.connector.Error as erro:
        print("Erro ao atualizar e-mail:", erro)

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def excluir_por_nome():
    nome = input("Digite o nome exato do cliente para excluir: ").strip()

    conexao = None
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = "DELETE FROM cliente WHERE nome = %s"
        cursor.execute(sql, (nome,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Cliente '{nome}' excluído com sucesso!")
        else:
            print(f"Nenhum cliente encontrado com o nome '{nome}'.")

    except mysql.connector.Error as erro:
        print("Erro ao excluir cliente:", erro)

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

def menu():
    criar_tabela()

    while True:
        print("\n==============================")
        print("     SISTEMA DE CLIENTES      ")
        print("==============================")
        print("1: Cadastrar")
        print("2: Listar clientes")
        print("3: Buscar cliente")
        print("4: Att email")
        print("5: Excluir nome")
        print("0: Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            atualizar_email()
        elif opcao == "5":
            excluir_por_nome()
        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()