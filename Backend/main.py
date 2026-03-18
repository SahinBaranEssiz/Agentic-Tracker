from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mesaj": "UI projesi icin FastAPI basariyla calisiyor!"}