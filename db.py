import sqlite3 as lite

# ! Criando o banco de dados
connect = lite.connect("lista.db")

def selecionar():
    lista_tarefa = []
    with connect:
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM tarefa;")
        
        rows = cursor.fetchall() # : Para atribuir todas as linhas resultantes da query na variavel "rows"
        for row in rows:
            lista_tarefa.append(row)
    return lista_tarefa

def inserir(item): # : Função para inserir uma tarefa no banco de dados
    with connect:
        cursor = connect.cursor()
        query = "INSERT INTO tarefa(nome) VALUES(?);"
        cursor.execute(query, item)


def deletar(item):
    with connect:
        cursor = connect.cursor()
        query = """
                    DELETE FROM tarefa
                        WHERE id=?;
                """
        cursor.execute(query, item)
        
def atualizar(item):
    cursor = connect.cursor()
    query = """
                UPDATE tarefa SET nome=?
                    WHERE id=?;
            """
    cursor.execute(query, item)

""" 
: Para criar a tabela "tarefa"
with connect:
    cursor = connect.cursor()
    cursor.execute(
        "CREATE TABLE tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)"
    )
"""