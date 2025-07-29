import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from wikibot import search_wikipedia, get_summary
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

class Wiki(BaseModel):
    name: str

@app.post("/wiki")
async def scrap_wikipedia(wiki: Wiki):
    """Endpoint to scrape Wikipedia for a given topic."""
    try:
        result = get_summary(wiki.name)
        return JSONResponse(content=jsonable_encoder({"summary": result}), status_code=200)
    except Exception as e:
        return JSONResponse(content=jsonable_encoder({"error": str(e)}), status_code=500)

@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Wikipedia Scraper API"}

uvicorn.run(app, host="0.0.0.0", port=8000)