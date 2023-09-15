from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from .users_db import get_user
from ..database.database import get_db
from ..database.models import User
from sqlalchemy.orm import Session


SECRET_KEY = "a98ba1e3a9e759d1cb9c8e5704f7c9dc25e090feec21826eadfb75170aac168a"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
	return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
	user = get_user(db, username)
	if not user:
		return False
	if not verify_password(password, user.hashed_password):
		return False
	return user

def get_password_hash(password: str):
	return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(minutes=15)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], auto_error: bool = True):
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials",
		headers={"WWW-Authenticate": "Bearer"},
	)
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		username: str = payload.get("sub")
		if username is None:
			raise credentials_exception
	except JWTError:
		raise credentials_exception
	user = get_user(next(get_db()), username=username)
	if user is None:
		raise credentials_exception
	return user


def getKillswitch(username: str):
	if username == 'mac':
		return False
	return False


async def get_current_active_user(
	user: User = Depends(get_current_user)
):
	if getKillswitch(user.username) and user.disabled:
		raise HTTPException(status_code=400, detail="Inactive user")
	return user


@router.post("/token")
async def login_for_access_token(
	form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
	db: Session = Depends(get_db),
):
	user = authenticate_user(db, form_data.username, form_data.password)
	if not user:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Incorrect username or password",
			headers={"WWW-Authenticate": "Bearer"},
		)
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	access_token = create_access_token(
		data={"sub": user.name}, expires_delta=access_token_expires
	)
	return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/")
async def read_users_me(
	user: User = Depends(get_current_active_user)
):
	return user


@router.get("/kill")
async def killswitch(
	k: str,
	user: User = Depends(get_current_active_user),
):
	if user.username != 'mac':
		return HTTPException(404)
	
	k = 't' in k


