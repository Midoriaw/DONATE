from pydantic import BaseModel

class UserOUT(BaseModel):
    username: str
    password: str


class LogOUT(BaseModel):
    username: str
    password: str


class rbOUT(BaseModel):
    RB_name: str
    email: str
    cardnumber: str
    donate: int


class donsteamOUT(BaseModel):
    steam_name:str
    email: str
    cardnumber: str
    donate: int


class donbrawlOUT(BaseModel):
    brawl_id: int
    username: str
    email: str
    cardnumber: str
    donate: int
