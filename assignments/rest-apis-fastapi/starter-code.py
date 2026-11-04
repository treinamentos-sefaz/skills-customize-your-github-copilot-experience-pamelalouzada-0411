# Código Inicial para a Atividade de APIs REST com FastAPI
# Instale as dependências com: pip install fastapi uvicorn
# Execute com: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Tarefa 1: Criar a primeira rota
app = FastAPI()


@app.get("/")
def read_root():
    # Retornar um dicionário com a chave "message"
    pass


# Tarefa 2: Listar e buscar livros
books = [
    # Adicione pelo menos 3 livros com id, title e author
]


@app.get("/books")
def list_books():
    # Retornar a lista completa de livros
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Buscar o livro pelo id e retornar 404 se não existir
    pass


# Tarefa 3: Adicionar livros com validação
class Book(BaseModel):
    id: int
    title: str
    author: str


@app.post("/books", status_code=201)
def create_book(book: Book):
    # Verificar duplicidade (409), adicionar à lista e retornar o livro
    pass
