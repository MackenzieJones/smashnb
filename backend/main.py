from fastapi import FastAPI
import uvicorn
from src.users import router as userRouter

app = FastAPI()

app.include_router(userRouter)

@app.get("/")
async def root():
	return f"Backend connection successful."

def main():
	uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
	main()