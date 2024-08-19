from fastapi.responses import RedirectResponse
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from .models import URLModel, Base
from .database import engine, get_db
from pydantic import BaseModel
import string
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

# Helper function to generate short codes
def generate_short_code(length: int = 6) -> str:
    base62 = string.ascii_letters + string.digits
    return ''.join(random.choice(base62) for _ in range(length))

# HTML Form Route
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API Route to shorten the URL
class URLCreate(BaseModel):
    original_url: str

@app.post("/shorten")
async def shorten_url(url_create: URLCreate, db: Session = Depends(get_db)):
    short_code = generate_short_code()
    
    while db.query(URLModel).filter(URLModel.short_code == short_code).first():
        short_code = generate_short_code()
    
    db_url = URLModel(original_url=url_create.original_url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    shortened_url = f"http://127.0.0.1:8000/{short_code}"
    return {"original_url": url_create.original_url, "shortened_url": shortened_url}

# Redirect to original URL using the short code
@app.get("/{short_code}")
async def get_original_url(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=db_url.original_url, status_code=307)
