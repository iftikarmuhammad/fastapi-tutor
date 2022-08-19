from datetime import datetime
from random import choices
from string import ascii_letters, digits

from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from . import models, schemas


SIZE = 6
ALPHANUM = ascii_letters + digits


def shorten_url(db):
    random_id = "".join(choices(ALPHANUM, k=SIZE))

    # repeat if random_id exist
    if db.query(exists().where(models.Shortener.shortId == random_id)).scalar():
        return shorten_url(db)

    return random_id


def get_short(db: Session, shortId: str):
    return db.query(models.Shortener).filter(models.Shortener.shortId == shortId).first()


def create_short(db: Session, short: schemas.ShortenerCreate):
    if not short.shortId:
        short.shortId = shorten_url(db)
    db_short = models.Shortener(shortId=short.shortId, url=short.url, createdAt=datetime.now())
    db.add(db_short)
    db.commit()
    db.refresh(db_short)
    return db_short