from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from .database import Base

class User(Base):
	__tablename__ = "user"
	id = Column(UUID(as_uuid=True), primary_key=True, index=True)
	name = Column(String, unique=True, index=True)
	role = Column(UUID(as_uuid=True), index=True)
	email = Column(String, unique=True, index=True)
	hashed_password = Column(String)


class Player(Base):
	__tablename__ = "player"
	id = Column(UUID(as_uuid=True), primary_key=True, index=True)
	user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"))
	name = Column(String, index=True)
	gamertag = Column(String, index=True)
	region = Column(String, index=True)
	avatar_path = Column(String, index=True)
	

class Slp(Base):
	__tablename__ = "slp"
	id = Column(UUID(as_uuid=True), primary_key=True, index=True)
	filepath = Column(String, index=True)
	description = Column(String, index=True)
	event_id = Column(UUID(as_uuid=True), ForeignKey("event.id"))
	player1_id = Column(UUID(as_uuid=True), ForeignKey("player.id"))
	player1_char = Column(String, index=True)
	player2_id = Column(UUID(as_uuid=True), ForeignKey("player.id"))
	player2_char = Column(String, index=True)


class Event(Base):
	__tablename__ = "event"
	id = Column(UUID(as_uuid=True), primary_key=True, index=True)
	name = Column(String, index=True)
	date = Column(DateTime, index=True)
	registrationEnd = Column(DateTime, index=True)
	numAttendees = Column(Integer)
	imagePath = Column(String)
	bracket = Column(String)
	stream = Column(String)
	region = Column(String, index=True)
	location = Column(String, index=True)
