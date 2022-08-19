from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/short-links/")
def shorten(short: schemas.ShortenerCreate, db: Session = Depends(get_db)):
    return {"data": crud.create_short(db=db, short=short)}


@app.get("/short-links/{shortId}")
def detail(shortId: str, db: Session = Depends(get_db)):
    return {"data": crud.get_short(db=db, shortId=shortId)}


@app.get("/r/{shortId}", response_class=RedirectResponse, status_code=302)
def redirect(shortId: str, db: Session = Depends(get_db)):
    short = crud.get_short(db=db, shortId=shortId)
    return short.url