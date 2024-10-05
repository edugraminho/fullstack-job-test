import httpx
import os
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException
from app.models.models import Account


router = APIRouter()

API_MOCK_URL = os.getenv("API_MOCK_URL")


async def process_create_account(account_data: dict, token: str, db: Session):
    url = f"{API_MOCK_URL}/account"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=account_data, headers=headers)

        if response.status_code == 201:
            account_details = response.json()

            new_account = Account(
                id=account_details.get("id"),
                tenant_id=account_details.get("tenantId"),
                name=account_details.get("name"),
                document=account_details.get("document"),
                account_type=account_details.get("accountType"),
                balance=account_details.get("balance"),
                status=account_details.get("status"),
                branch=account_details.get("branch"),
                number=account_details.get("number"),
                created_at=account_details.get("createdAt"),
                updated_at=account_details.get("updatedAt"),
            )

            db.add(new_account)
            db.commit()
            db.refresh(new_account)

            return account_details
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail={
                    "message": response.json().get("message"),
                    "error": "Request Error",
                    "statusCode": response.status_code,
                },
            )


async def process_account_details(account_id: str, token: str):
    url = f"{API_MOCK_URL}/account/{account_id}"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            if response.content:
                return response.json()
            else:
                return {"message": "Account not found", "status": 200}
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail={
                    "message": response.json().get("message"),
                    "error": "Request Error",
                    "statusCode": response.status_code,
                },
            )


async def process_account_statement(account_id: str, token: str):
    url = f"{API_MOCK_URL}/account/{account_id}/statement"
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail={
                    "message": response.json().get("message"),
                    "error": "Request Error",
                    "statusCode": response.status_code,
                },
            )
