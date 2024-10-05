import httpx
import os
from fastapi import HTTPException


API_MOCK_URL = os.getenv("API_MOCK_URL")


async def process_ted_transfer(token: str, transfer_data: dict):
    url = f"{API_MOCK_URL}/transaction/ted"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Payer-Id": transfer_data.get("recipientDocument"),
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=transfer_data, headers=headers)

        if response.status_code == 201:
            return response.json()
        else:
            try:
                error_message = response.json().get("message", "Unknown error")
            except ValueError:
                error_message = response.text

            raise HTTPException(
                status_code=response.status_code,
                detail={
                    "message": error_message,
                    "error": "Request Error",
                    "statusCode": response.status_code,
                },
            )


async def process_pix_transfer(token: str, account_id: str, transfer_data: dict):
    url = f"{API_MOCK_URL}/transaction/pix/{account_id}/pay"
    headers = {
        "Authorization": f"Bearer {token}",
        "accountId": account_id,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=transfer_data, headers=headers)

        if response.status_code == 201:
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


async def process_pay_billet(payment_data: dict, token: str):
    url = f"{API_MOCK_URL}/transaction/billet"
    print(payment_data)
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Payer-Id": payment_data.get("accountId"),
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payment_data, headers=headers)

        if response.status_code == 201:
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


async def process_internal_transfer(transfer_data: dict, token: str):
    url = f"{API_MOCK_URL}/transaction/internal"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Payer-Id": transfer_data.get("sourceAccountId"),
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=transfer_data, headers=headers)

        if response.status_code == 201:
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
