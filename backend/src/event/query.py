from datetime import datetime
from sqlalchemy.orm import Session
from src.database.models import Event

def getEvents(
	db: Session,
	fromDate: datetime = None,
	toDate: str = None,
	region: str = None,
	searchString: str = None,
	skip: int = None,
	limit: int = None
):
	query = db.query(Event)

	if fromDate is not None:
		query = query.filter(Event.date >= fromDate)
	if toDate is not None:
		query = query.filter(Event.date <= toDate)

	if region is not None:
		query = query.filter(Event.region == region)

	# TODO: Improve search functionality
	if searchString is not None:
		query = query.filter(Event.name.contains(searchString))

	if skip is not None:
		query = query.offset(skip)
	if limit is not None:
		query = query.limit(limit)

	return query.all()