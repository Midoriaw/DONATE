from fastapi import HTTPException, Depends
from passlib.handlers.bcrypt import bcrypt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from src.models import RegORM, DonateRb, DonateBrawl, DonateSteam, Base
from src.schema import Personal_accountOUT

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_users(db: AsyncSession, username: str, password:str):
    new_user = await db.execute(select(RegORM).where(RegORM.username == username))
    if new_user.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Пользователь уже существует")

    hashed_password = pwd_context.hash(password)
    new_user = RegORM(username=username, password=hashed_password)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def log_users(db: AsyncSession, user: str, password: str):
    result = await db.execute(select(RegORM).where(RegORM.username == user))
    user = result.scalar_one_or_none()
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=404, detail="Неверное имя пользователя или пароль")
    return user


async def don_rb(db: AsyncSession, RB_name: str, email: str, cardnumber: str, donate: int):
    new_don = DonateRb(RB_name=RB_name, email=email, cardnumber=cardnumber, donate=donate)
    db.add(new_don)
    await db.commit()
    await db.refresh(new_don)
    return new_don

async def don_steam(db: AsyncSession, steam_name: str, email: str, cardnumber: str, donate: int):
    new_don = DonateSteam(steam_name=steam_name, email=email, cardnumber=cardnumber, donate=donate)
    db.add(new_don)
    await db.commit()
    await db.refresh(new_don)
    return new_don

async def don_brawl(db: AsyncSession, brawl_id:int, username:str, email:str, cardnumber: str, donate: int):
    new_don = DonateBrawl(brawl_id=brawl_id, username=username, email=email, cardnumber=cardnumber, donate=donate)
    db.add(new_don)
    await db.commit()
    await db.refresh(new_don)
    return new_don


async def get_personal_account(db: AsyncSession,user_id: int, password: str):
    result = await db.execute(select(RegORM).where(RegORM.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=404, detail="Неверный пароль")


    result_Rb = (await db.execute(select(DonateRb).where(DonateRb.user_id == user_id)))
    Rb = result_Rb.scalars().all()

    result_steam = (await db.execute(select(DonateSteam).where(DonateSteam.user_id == user_id)))
    steam = result_steam.scalars().all()

    result_brawl = (await db.execute(select(DonateSteam).where(DonateSteam.user_id == user_id)))
    brawl = result_brawl.scalars().all()

    return {

        "id": user.id,
        "username": user.username,
        "Rb": Rb,
        "steam": steam,
        "brawl": brawl
    }
