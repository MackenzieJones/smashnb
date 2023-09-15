from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base

class User(Base):
	__tablename__ = "user"

	id = Column(UUID(as_uuid=True), primary_key=True, index=True)
	name = Column(String, unique=True, index=True)
	role = Column(UUID(as_uuid=True), index=True)
	email = Column(String, unique=True, index=True)
	hashed_password = Column(String)


class Slp(Base):
	__tablename__ = "slp"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String, index=True)
	description = Column(String, index=True)
	player1 = Column(UUID(as_uuid=True), ForeignKey("user.id"))
	player2 = Column(UUID(as_uuid=True), ForeignKey("user.id"))
