import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='crud',
)
cursor = conexao.cursor()

# CRUD
comando = f'SELECT * FROM produtos'
cursor.execute(comando)
resultado = cursor.fetchall()  # ler
print(resultado)

# comando=""# comando
# conexao.commit() # edita o banco de dados
# resultado = cursor.fetchall() #ler
# cursor.execute(comando)# executar

# UPDATE

# nome_produto =# CREATE
#
# # nome_produto = "chocolate"
#
# # valor = 15
#
# # comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#
# # cursor.execute(comando)
#
# # conexao.commit() # edita o banco de dados
#
#
#
# # READ
#
# # comando = f'SELECT * FROM vendas'
#
# # cursor.execute(comando)
#
# # resultado = cursor.fetchall() # ler o banco de dados
#
# # print(resultado)

# valor = 6

# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados


# DELETE

# nome_produto = "todynho"

# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'

# cursor.execute(comando)


cursor.close()
conexao.close()
