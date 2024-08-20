import sqlite3
import os

# Defina o caminho absoluto do diretório onde o banco de dados deve ser salvo
caminho_banco = r'D:\Projetos\WMC\Data_Analytics_WoMakersCode_Bootcamp\banco_de_dados_SQL\banco'

# Conecte-se ao banco de dados usando o caminho absoluto
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))')
#cursor.execute('CREATE TABLE gerente(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefone INT')

#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (1, "Isadora", "França", "isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (2, "Maria", "Salvador", "maria@gmail.com", 789123)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (3, "José", "São Paulo", "jose@gmail.com", 456789)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (4, "Marcia", "Rio de Janeiro", "marcia@gmail.com", 120325)')
#cursor.execute('INSERT INTO usuario(id, nome, endereco, email, telefone) VALUES (5, "Marcia", "Rio de Janeiro", "marcia@gmail.com", 120325)')

#cursor.execute('INSERT INTO gerente(id, nome, endereco, email) VALUES (9, "Fernanda", "Paris", "fernanda@gmail.com")')

#cursor.execute('DELETE FROM usuario WHERE id=5')
#cursor.execute('UPDATE usuario SET endereco = "Minas Gerais" WHERE nome = "José"')



# ORDER BY E DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')

# DISTINCT E LIMIT
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')

# GROUP BY E HAVING -- Não conseguimos usar para filtrar a clausula WHERE depois do GROUP BY, e sim HAVING
#para usar WHERE teríamos que colocar antes de GROUP BY
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')

#JOIN's
# JOIN - INNER JOIN
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerente ON usuario.id = gerente.id')

# JOIN - LEFT JOIN
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerente ON usuario.nome = gerente.nome')

# JOIN - RIGHT JOIN
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerente ON usuario.nome = gerente.nome')
 
# JOIN - FULL JOIN  -- LEFT + RIGHT JOIN
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerente ON usuario.nome = gerente.nome')

# SUB-CONSULTAS
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerente)')

for usuario in dados:
    print(usuario)


conexao.commit()
conexao.close()