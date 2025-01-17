import sqlite3

# Defina o caminho absoluto do diretório onde o banco de dados deve ser salvo
caminho_banco = r'D:\Projetos\WMC\Data_Analytics_WoMakersCode_Bootcamp\desafios\SQL\banco_dados'

# Conecte-se ao banco de dados usando o caminho absoluto
conexao = sqlite3.connect(caminho_banco)
cursor = conexao.cursor()

# 1) CRIANDO A TABELA NO BD
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(50))')

# 2) INSERINDO DADOS NO BD
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, "Julia", "21", "Desenvolvimento de Sistemas")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Mario", "28", "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Marcos", "21", "Educação Física")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Lauren", "20", "Educação Física")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Marcos", "19", "Biologia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "Paulo", "45", "Biologia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (7, "Bruno", "25", "Física")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (8, "Tatiana", "18", "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (9, "Larissa", "31", "Direito")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (10, "Maria", "50", "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (11, "Juliana", "20", "Administração")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (12, "Julia", "30", "Engenharia")')

# 3)a. Selecionando todos os registros da tabela ALUNOS

# b. Selecionando NOME E IDADE somente dos alunos com mais de 20 anos
#dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')

# c. Selecionando somente os alunos do curso de "Engenharia"
#dados = cursor.execute('SELECT nome FROM alunos WHERE curso = "Engenharia" ORDER BY nome')

# c. Contar o número total de alunos na tabela
#dados = cursor.execute('SELECT COUNT (nome) FROM alunos')

# 4)a. Atualizar a idade de um alunos específico na tabela
#cursor.execute('UPDATE alunos SET idade = 19 WHERE nome = "Marcos"')

# b.Remover um aluno pelo seu ID
#cursor.execute('DELETE FROM alunos WHERE id=12')


'''for alunos in dados:
    print(alunos)'''

# 5) Criar uma tbela chamada 'clientes' e inserir alguns registros
#cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT, CONSTRAINT PK PRIMARY KEY (id))')
 ## inserindo registros
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Marcelo", 18, 20.45)') # usar . para separador de float
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Bruna", 45, 350.65)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Marcos", 21, 75.18)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Lauren", 20, 15.00)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Maiara", 22, 85.25)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (6, "Elenice", 65, 5.28)')

# 6)a. Selecionar nome e idade dos clientes com idade superior a 30 anos
#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')

# b. Calcular o saldo médio dos clientes
#dados = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')

# c. Encontrar o cliente com o maior saldo
#dados = cursor.execute('SELECT MAX(saldo) AS maior_saldo FROM clientes')

# b. Contar quantos clinetes tem o saldo acima de 1000
#dados = cursor.execute('SELECT COUNT(*) AS qtd_clientes FROM clientes WHERE saldo>1000')

# 7)a. Atualizar o saldo de um cliente específico
#cursor.execute('UPDATE clientes SET saldo = 1350.75 WHERE nome = "Elenice"')

# b. Remover um cliente pelo seu ID
#cursor.execute('DELETE FROM clientes WHERE id=1')

'''for clientes in dados:
    print(clientes)'''

# 8) Criar uma tabela chamada 'compras'
#cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
 ## inserindo registros
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 2, "teclado", 150.28)') # usar . para separador de ,
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 2, "mouse", 75.40)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 7, "monitor", 900.49)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (4, 3, "mouse", 30.99)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (5, 4, "bombom", 14.98)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (6, 6, "celular", 895.98)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (7, 8, "freezer", 7045.98)') # máx 6digitos real??

# Verificar as compras feitas pelos clientes da tabela cliente
#dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes JOIN compras ON clientes.id = compras.cliente_id')

'''for compras in dados:
    print(compras)'''


conexao.commit()
conexao.close()