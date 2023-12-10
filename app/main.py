from fastapi import FastAPI

from app.apis import multimodal, text

app = FastAPI()

app.include_router(text.router, prefix="/text", tags=["Text"])
app.include_router(multimodal.router, prefix="/multimodal", tags=["Multimodal"])
