from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Rota raiz
@app.get("/")
def home():
    return {"Ola" : "Mundo"}

# Criar model
class Usuario(BaseModel):
    id: int
    email: str
    senha: str

# Criar base de dados
base_de_dados = [
    Usuario(id=1, email="email1@email.com.br", senha="senha123"),
    Usuario(id=2, email="email2@email.com.br", senha="senha321")
]

# Rota Get All
@app.get("/usuarios")
def get_all_users():
    return base_de_dados

# Rota Get Id
@app.get("/usuarios/{id}")
def get_user_by_id(id: int):
    for usuario in base_de_dados:
        if(usuario.id == id):
            return usuario
    return {"Status": 404, "Mensagem": "Usuário não encontrado."}

# Rota Create User
@app.post("/usuarios")
def create_user(user: Usuario):
    for usuario in base_de_dados:
        if(usuario.email == user.email):
            return {"Status": 406, "Mensagem": "Usuário já cadastrado."}
    base_de_dados.append(user)
    return {"Status": 201, "Mensagem": "Usuário criado."}
