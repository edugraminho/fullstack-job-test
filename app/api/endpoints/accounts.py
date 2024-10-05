import httpx
import os
from fastapi import APIRouter, HTTPException, Depends
from app.database.redis_cache import get_access_token
from app.models.models import AccountCreate

router = APIRouter()

API_MOCK_URL = os.getenv("API_MOCK_URL")


@router.post("/accounts/")
async def create_account(
    account: AccountCreate, token: str = Depends(get_access_token)
):
    url = f"{API_MOCK_URL}/account"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "accountType": account.account_type,
        "name": account.name,
        "document": account.document,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Error creating account"
            )


@router.get("/accounts/{account_id}")
async def get_account_details(account_id: str, token: str = Depends(get_access_token)):

    url = f"{API_MOCK_URL}/account/{account_id}"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail="Error fetching account details",
            )


@router.get("/accounts/{account_id}/statement")
async def get_account_statement(
    account_id: str, token: str = Depends(get_access_token)
):

    url = f"{API_MOCK_URL}/account/{account_id}/statement"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail="Error fetching account statement",
            )
