from fastapi import FastAPI

app = FastAPI(title="simple-API", version="1.0.0")

# - Testing -
@app.get("/")
def read_root():
    return {
        "status" : "oke",
        "status": "Engine is running smoothly"
    }