import os
from fastapi import APIRouter, Depends
from app.database.redis_cache import get_access_token
from app.models.models import AccountCreate
from app.services.accounts_service import (
    process_create_account,
    process_account_details,
    process_account_statement,
)

router = APIRouter()

API_MOCK_URL = os.getenv("API_MOCK_URL")


@router.post("/accounts/")
async def create_account(
    account: AccountCreate, token: str = Depends(get_access_token)
):
    data = account.model_dump(by_alias=True)
    return await process_create_account(data, token)


@router.get("/accounts/{account_id}")
async def get_account_details(account_id: str, token: str = Depends(get_access_token)):
    return await process_account_details(account_id, token)


@router.get("/accounts/{account_id}/statement")
async def get_account_statement(
    account_id: str, token: str = Depends(get_access_token)
):
    return await process_account_statement(account_id, token)
