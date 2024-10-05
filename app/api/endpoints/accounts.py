import os
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database.redis_cache import get_access_token
from app.models.models import AccountCreate, Account
from app.services.accounts_service import (
    process_create_account,
    process_account_details,
    process_account_statement,
)
from app.database.db_connection import get_db

router = APIRouter()

API_MOCK_URL = os.getenv("API_MOCK_URL")


@router.post("/accounts/")
async def create_account(
    account: AccountCreate,
    token: str = Depends(get_access_token),
    db: Session = Depends(get_db),
):
    data = account.model_dump(by_alias=True)
    return await process_create_account(data, token, db)


@router.get("/accounts/open")
async def get_open_accounts(db: Session = Depends(get_db)):
    open_accounts = db.query(Account).all()

    if not open_accounts:
        return {"message": "No open accounts found", "status": 404}

    return {"open_accounts": open_accounts}


@router.get("/accounts/total-balance")
async def get_total_balance(db: Session = Depends(get_db)):
    total_balance = db.query(func.sum(Account.balance)).scalar()

    if total_balance is None:
        return {"message": "No accounts found", "total_balance": 0}

    return {"total_balance": total_balance}


@router.get("/accounts/{account_id}")
async def get_account_details(account_id: str, token: str = Depends(get_access_token)):
    return await process_account_details(account_id, token)


@router.get("/accounts/{account_id}/statement")
async def get_account_statement(
    account_id: str, token: str = Depends(get_access_token)
):
    return await process_account_statement(account_id, token)
