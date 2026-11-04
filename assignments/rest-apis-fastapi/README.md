# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Nesta atividade, você vai criar uma API REST com o framework FastAPI, aprendendo a definir rotas, retornar dados em JSON, validar entradas com modelos Pydantic e tratar erros com códigos HTTP adequados.

## 📝 Tarefas

### 🛠️ Criar a primeira rota

#### Descrição
Configure a aplicação FastAPI e crie uma rota `GET /` que retorna uma mensagem de boas-vindas. Essa é a base para as próximas tarefas.

#### Requisitos
O programa concluído deve:

- Criar um objeto `app = FastAPI()`.
- Definir a rota `GET /` que retorna um dicionário com a chave `"message"`.
- Ser executado com `uvicorn main:app --reload` sem erros.
- Responder em `http://127.0.0.1:8000/` com a mensagem definida.


### 🛠️ Listar e buscar livros

#### Descrição
Crie uma lista de livros em memória e exponha rotas para listar todos os livros e buscar um livro pelo seu identificador. Use o parâmetro de caminho para identificar o livro.

#### Requisitos
O programa concluído deve:

- Manter uma lista de pelo menos 3 livros, cada um com `id`, `title` e `author`.
- Definir `GET /books` que retorna a lista completa.
- Definir `GET /books/{book_id}` que retorna o livro correspondente ao `id` informado.
- Retornar status `404` com a mensagem `"Livro não encontrado"` quando o `id` não existir.


### 🛠️ Adicionar livros com validação

#### Descrição
Permita que o cliente cadastre novos livros enviando dados no corpo da requisição. Use um modelo Pydantic para validar os dados recebidos antes de salvá-los.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic `Book` com os campos `id`, `title` e `author`.
- Definir `POST /books` que recebe um `Book` no corpo da requisição e o adiciona à lista.
- Retornar status `201` e o livro criado quando o cadastro for bem-sucedido.
- Retornar status `422` automaticamente quando faltar algum campo obrigatório.
- Retornar status `409` com a mensagem `"Já existe um livro com este id"` quando o `id` já estiver cadastrado.
