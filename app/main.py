from fastapi import FastAPI

from app.apis import text

app = FastAPI()

app.include_router(text.router, prefix="/text", tags=["Text"])
