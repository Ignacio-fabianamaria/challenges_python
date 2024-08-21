# 🚀 Bootcamp Back-End Python e Django

## 📚 Exercícios - Banco de Dados

### 1. 🏗️ Criação de Tabela
Crie uma tabela chamada **"alunos"** com os seguintes campos:
- `id` (inteiro)
- `nome` (texto)
- `idade` (inteiro)
- `curso` (texto)

### 2. 📝 Inserção de Registros
Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

### 3. 🔍 Consultas Básicas
Escreva consultas SQL para realizar as seguintes tarefas:
- **a)** Selecionar todos os registros da tabela **"alunos"**.
- **b)** Selecionar o nome e a idade dos alunos com mais de 20 anos.
- **c)** Selecionar os alunos do curso de **"Engenharia"** em ordem alfabética.
- **d)** Contar o número total de alunos na tabela.

### 4. 🔧 Atualização e Remoção
- **a)** Atualize a idade de um aluno específico na tabela.
- **b)** Remova um aluno pelo seu ID.

### 5. 🏗️ Criação de Tabela e Inserção de Dados
Crie uma tabela chamada **"clientes"** com os seguintes campos:
- `id` (chave primária)
- `nome` (texto)
- `idade` (inteiro)
- `saldo` (float)

Insira alguns registros de clientes na tabela.

### 6. 🔍 Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
- **a)** Selecione o nome e a idade dos clientes com idade superior a 30 anos.
- **b)** Calcule o saldo médio dos clientes.
- **c)** Encontre o cliente com o saldo máximo.
- **d)** Conte quantos clientes têm saldo acima de 1000.

### 7. 🔧 Atualização e Remoção com Condições
- **a)** Atualize o saldo de um cliente específico.
- **b)** Remova um cliente pelo seu ID.

### 8. 🔗 Junção de Tabelas
Crie uma segunda tabela chamada **"compras"** com os seguintes campos:
- `id` (chave primária)
- `cliente_id` ( chave estrangeira referenciando o ID da tabela **"clientes"**)
- `produto` (texto)
- `valor` (real)

Insira algumas compras associadas a clientes existentes na tabela **"clientes"**.

Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
