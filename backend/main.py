from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.routes import appRouter

app = FastAPI()

app.include_router(appRouter)

@app.get("/")
async def root():
	return f"Backend connection successful."

origins = [
	"http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def main():
	uvicorn.run(app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
	main()