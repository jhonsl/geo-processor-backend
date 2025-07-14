from fastapi import FastAPI
from routers import geo_processor

app = FastAPI()
app.include_router(geo_processor.router)

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}