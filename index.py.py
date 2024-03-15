import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def example() -> str:
    return "OLA SENAI!!"

if __name__ == "__main__":
    uvicorn.run(app, port=8000)