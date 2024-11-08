
import psycopg2


# Estabelecendo a conexão com o Banco de dados
def conectardb() -> object:
    conexao = psycopg2.connect(database="minicursobd",
                               host="localhost",
                               user="postgres",
                               password="Narnia&05",
                               port="5432")
    return conexao


# Chame a função para testar a conexão
conexao = conectardb()


# Inserir Usuário
def inserir_usuario(nome, email):
    conexao = conectardb()  # Estabelece conexão com o banco de dados.
    cursor = conexao.cursor()  # Cria um cursor para executar comandos SQL.
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))

conexao.commit()                      # Salva (confirma) a transação no banco de dados.
    cursor.close()                        # Fecha o cursor.
    conexao.close()