from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from ..database.database import get_db
from typing import Optional, List
from datetime import datetime

from . import query
from src.database.models import Event

router = APIRouter()


@router.get('/event/list')
def getEvents (
	db: Session = Depends(get_db),
	fromDate: Optional[datetime] = Query(None, description="Start date for search (YYYY-MM-DD)"),
	toDate: Optional[datetime] = Query(None, description="End date for search (YYYY-MM-DD)"),
	region: Optional[str] = Query(None, description="Region for search"),
	searchString: Optional[str] = Query(None, description="Search string"),
	skip: Optional[int] = Query(0, ge=0, description="Number of items to skip"),
	limit: Optional[int] = Query(10, ge=1, le=100, description="Number of items to return")
):
	return query.getEvents(
		db,
		fromDate,
		toDate,
		region,
		searchString,
		skip,
		limit,
	)

@router.post('/event/new')
def makeEvent(
	db: Session = Depends(get_db),
):
	pass