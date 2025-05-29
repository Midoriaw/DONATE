from fastapi import FastAPI, Depends, HTTPException
from passlib.context import CryptContext
from src.database import get_db, lifespan
from src.crud import create_users, log_users, don_rb, don_steam, don_brawl
from src.schema import UserOUT, LogOUT, rbOUT, donsteamOUT, donbrawlOUT
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Base, RegORM, DonateRb,DonateBrawl,DonateSteam

app = FastAPI(lifespan=lifespan)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/users", tags=["Регистрация"])
async def user(user:UserOUT, db: AsyncSession = Depends(get_db)):
    new_user = await create_users(db, user.username, user.password)
    return {"id": new_user.id, "username":new_user.username}

@app.post("/logusers", tags=["Авторизация"])
async def log(login:LogOUT, db: AsyncSession = Depends(get_db)):
    user = await log_users(db, login.username, login.password)
    return {
            "mess": "Вход выполнен успешно!",
            "user_id": user.id,
            "username": user.username


    }


@app.post("/donROBLOX",tags=["Донат в роблокс"])
async def rb(roblox: rbOUT, db: AsyncSession = Depends(get_db)):
   new_don_rb = await don_rb(db, roblox.RB_name, roblox.email, roblox.cardnumber, roblox.donate)
   return{
    "mess": "Операция выполнена успешно!",
    "new_don_rb_id": new_don_rb.id,
    }

@app.post("/donsteam", tags=["Донат в стим"])
async def steam(steamm: donsteamOUT,db: AsyncSession = Depends(get_db)):
    new_don_steam = await don_steam(db, steamm.steam_name, steamm.email, steamm.cardnumber, steamm.donate)
    return {
    "mess": "Операция выполнена успешно!",
    "new_don_steam_id": new_don_steam.id,
    }

@app.post("/donbrawl", tags=["Донат в бравл"])
async def brawl(brawlik: donbrawlOUT,db: AsyncSession = Depends(get_db)):
    new_don_brawl = await don_brawl(db, brawlik.brawl_id, brawlik.username, brawlik.email, brawlik.cardnumber, brawlik.donate)
    return {
    "mess": "Операция выполнена успешно!",
    "new_don_brawl_id": new_don_brawl.id,
    }