from datetime import datetime

from pydantic import BaseModel


class ShortenerBase(BaseModel):
    shortId: str | None = None
    url: str
    createdAt: datetime | None = None


class ShortenerCreate(ShortenerBase):
    pass


class Shortener(ShortenerBase):
    class Config:
        orm_mode = True

