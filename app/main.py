from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello() -> dict[str, str]:
    return {"hello": "world"}
