from fastapi import FastAPI

app = FastAPI()

@app.get("/server")
def root():
    return {"message": "Hello Docker"}