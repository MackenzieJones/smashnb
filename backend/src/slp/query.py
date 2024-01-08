from datetime import datetime
from sqlalchemy import UUID
from sqlalchemy.orm import Session
from src.database.models import Slp, Event, Player

def getSlps(
	db: Session,
	fromDate: datetime = None,
	toDate: str = None,
	region: str = None,
	eventID: UUID = None,
	player1: UUID = None,
	player2: UUID = None,
	skip: int = None,
	limit: int = None
):
	query = (
		db.query(Slp, Player)
		.join(Event, Event.id == Slp.event_id)
	)

	if player1 is not None:
		query = query.join(Player, (Player.id == player1))
	if player2 is not None:
		query = query.join(Player, (Player.id == player2))

	if fromDate is not None:
		query = query.filter(Event.date >= fromDate)
	if toDate is not None:
		query = query.filter(Event.date <= toDate)

	if region is not None:
		query = query.filter(Event.region == region)

	if eventID is not None:
		query = query.filter(Slp.event_id == eventID)

	query = query.offset(skip)
	query = query.limit(limit)

	return query.all()