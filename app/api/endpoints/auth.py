import os
from fastapi import APIRouter, HTTPException
from app.services.auth_service import create_tenant_service, login_to_baas_api
from app.database.redis_cache import store_access_token, get_access_token

router = APIRouter()

API_MOCK_URL = os.getenv("API_MOCK_URL")


@router.post("/auth/login")
async def login():
    client_id, client_secret = await create_tenant_service()
    access_token = await login_to_baas_api(client_id, client_secret)

    store_access_token(access_token)

    if access_token:
        return {"message": "Login successful", "access_token": access_token}
    else:
        raise HTTPException(status_code=500, detail="Failed to log in")
