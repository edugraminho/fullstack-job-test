import httpx
from fastapi import HTTPException
import os


API_MOCK_URL = os.getenv("API_MOCK_URL")


async def create_tenant_service():
    create_tenant_url = f"{API_MOCK_URL}/tenant"
    headers = {"X-Mock": "true"}

    async with httpx.AsyncClient() as client:
        response = await client.post(create_tenant_url, headers=headers)

        if response.status_code == 201:
            data = response.json()
            client_id = data.get("clientId")
            client_secret = data.get("clientSecret")
            if client_id and client_secret:
                return client_id, client_secret
            else:
                raise HTTPException(
                    status_code=500, detail="No clientId or clientSecret in response"
                )
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Failed to create tenant"
            )


async def login_to_baas_api(client_id, client_secret):
    login_url = f"{API_MOCK_URL}/auth/login"

    login_data = {"clientId": client_id, "clientSecret": client_secret}

    async with httpx.AsyncClient() as client:
        response = await client.post(login_url, json=login_data)

        if response.status_code == 201:
            data = response.json()
            access_token = data.get("access_token")
            if access_token:
                return access_token
            else:
                raise HTTPException(
                    status_code=500, detail="No access_token in response"
                )
        else:
            raise HTTPException(
                status_code=response.status_code, detail="Failed to log in"
            )
