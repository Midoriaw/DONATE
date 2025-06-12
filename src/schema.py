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

class Personal_accountOUT(BaseModel):
    id: int
    username: str
    Rb: List[DonateRb]
    steam: List[DonateSteam]
    brawl: List[DonateBrawl]

    class Config:
        from_orm=True


class PersonalAccountIN(BaseModel):
    password: str