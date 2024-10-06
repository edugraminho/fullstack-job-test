import os
from fastapi import APIRouter, Depends
from app.database.redis_cache import get_access_token
from app.models.models import TEDTransfer, PIXTransfer, BilletPayment, InternalTransfer
from app.services.transaction_service import (
    process_ted_transfer,
    process_pix_transfer,
    process_pay_billet,
    process_internal_transfer,
)

router = APIRouter()

API_MOCK_URL = os.getenv("API_MOCK_URL")


@router.post("/transaction/ted")
async def ted_transfer(
    transfer_data: TEDTransfer, token: str = Depends(get_access_token)
):
    data = transfer_data.model_dump(by_alias=True)
    return await process_ted_transfer(token, data)


@router.post("/transaction/pix/{account_id}/pay")
async def pix_transfer(
    account_id: str,
    transfer_data: PIXTransfer,
    token: str = Depends(get_access_token),
):
    data = transfer_data.model_dump(by_alias=True)
    return await process_pix_transfer(token, account_id, data)


@router.post("/transaction/billet")
async def pay_billet(
    payment_data: BilletPayment, token: str = Depends(get_access_token)
):
    data = payment_data.model_dump(by_alias=True)
    return await process_pay_billet(data, token)


@router.post("/transaction/internal")
async def internal_transfer(
    transfer_data: InternalTransfer, token: str = Depends(get_access_token)
):
    data = transfer_data.model_dump(by_alias=True)
    return await process_internal_transfer(data, token)
