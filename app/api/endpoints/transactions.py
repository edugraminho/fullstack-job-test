import httpx
import os
from fastapi import APIRouter, HTTPException, Depends
from app.database.redis_cache import get_access_token
from app.models.models import TEDTransfer, PIXTransfer, BilletPayment, InternalTransfer

router = APIRouter()

API_MOCK_URL = os.getenv("API_MOCK_URL")


@router.post("/transaction/ted")
async def ted_transfer(
    transfer_data: TEDTransfer, token: str = Depends(get_access_token)
):
    url = f"{API_MOCK_URL}/transaction/ted"
    headers = {"Authorization": f"Bearer {token}"}
    data = transfer_data.model_dump(by_alias=True)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Error processing TED transfer"
            )


@router.post("/transaction/pix")
async def pix_transfer(
    transfer_data: PIXTransfer, token: str = Depends(get_access_token)
):
    url = f"{API_MOCK_URL}/transaction/pix/{transfer_data.account_id}/pay"
    headers = {"Authorization": f"Bearer {token}"}

    data = transfer_data.model_dump(by_alias=True)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Error processing PIX transfer"
            )


@router.post("/transaction/billet")
async def pay_billet(
    payment_data: BilletPayment, token: str = Depends(get_access_token)
):
    url = f"{API_MOCK_URL}/transaction/billet"
    headers = {"Authorization": f"Bearer {token}"}
    data = payment_data.model_dump(by_alias=True)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Error paying billet"
            )


@router.post("/transaction/internal")
async def internal_transfer(
    transfer_data: InternalTransfer, token: str = Depends(get_access_token)
):
    url = f"{API_MOCK_URL}/transaction/internal"
    headers = {"Authorization": f"Bearer {token}"}
    data = transfer_data.model_dump(by_alias=True)

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail="Error processing internal transfer",
            )
