import sqlite3
import database_records

conexao = sqlite3.connect("/home/fabynando/Documentos/faby/challenges_python/07-database/database")
cursor = conexao.cursor()

# Excluindo a tabela 'alunos' se ela já existir
cursor.execute('DROP TABLE IF EXISTS alunos')

# Criando a tabela 'alunos'
cursor.execute('''
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INT NOT NULL,
    curso TEXT NOT NULL
)
''')

# Inserindo registros na tabela 'alunos'
cursor.executemany('''
INSERT INTO alunos (nome, idade, curso)
VALUES (?, ?, ?)
''', database_records.alunos)

# Excluindo a tabela 'clientes' se ela já existir
cursor.execute('DROP TABLE IF EXISTS clientes')

# Criando a tabela 'clientes'
cursor.execute('''
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INT NOT NULL,
    saldo REAL NOT NULL
)
''')

# Inserindo registros na tabela 'clientes'
cursor.executemany('''
INSERT INTO clientes(nome, idade, saldo)
VALUES (?, ?, ?)
''', database_records.clientes)


"""data = cursor.execute('SELECT * FROM alunos')
for alunos in data:
    print(alunos)"""

conexao.commit()
conexao.close()
