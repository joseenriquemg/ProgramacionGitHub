from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#app = FastAPI()
oautha2 = OAuth2PasswordBearer(tokenUrl="login")

# Definimos el algoritmo de encriptacion
ALGORITHM ="HS256"

# Duracion del token
ACCESS_TOKEN_EXPIRE_MINUTES = 10

# Clave que se utilizará como semilla para generar el token
# openssl rand -hex 32
SECRET_KEY = "5f4d1a010a9436eb0e57cd56ceed8515ffd0eea5995c88ac3b282c70616bf207"

# Objeto que se utilizara para el calculo del hash y
#La verificacion de contraseñas
password_hash = PasswordHash.recommended()

router = APIRouter()

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disable: bool

class userDB(User):
    password: str

users_db = {
    "jenrimg": {
        "username" : "jenrimg",
        "fullname" : "Jose Enrique Muñoz Galloso",
        "email" : "jenrimg2005@gmail.com",
        "disable" : False,
        "password" : "12345"
    }

}

@router.post("/register", status_code=201)
def register(user: userDB):
    if(user.username not in users_db):
        hashed_password = password_hash.hash(user.password)
        user.password = hashed_password
        users_db[user.username] = user
        return user
    else: 
        raise HTTPException(status_code=409, detail="El usuario ya existe")
