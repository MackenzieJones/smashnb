from sqlalchemy.orm import Session
from ..database.models import *

def get_user(db: Session, email: str) -> User:
	query = (
		db.query(User)
		.filter(User.email == email)
	)

	return query.one_or_none()
