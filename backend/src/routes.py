from fastapi import APIRouter
from src.user import router as userRouter
from src.event import router as eventRouter
from src.slp import router as slpRouter

appRouter = APIRouter()
appRouter.include_router(userRouter)
appRouter.include_router(eventRouter)
appRouter.include_router(slpRouter)
