import uuid
from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from .base import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tenant_id = Column(UUID(as_uuid=True), nullable=False)
    account_type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    document = Column(String, nullable=False)
    status = Column(String, nullable=False)
    balance = Column(Float, nullable=False, default=0.0)
    branch = Column(String, nullable=False)
    number = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AccountCreate(BaseModel):
    account_type: str = Field(..., alias="accountType")
    name: str
    document: str


class TEDTransfer(BaseModel):
    account_id: str = Field(..., alias="accountId")
    amount: float
    recipient_name: str = Field(..., alias="recipientName")
    recipient_document: str = Field(..., alias="recipientDocument")
    recipient_bank: str = Field(..., alias="recipientBank")
    recipient_branch: str = Field(..., alias="recipientBranch")
    recipient_account: str = Field(..., alias="recipientAccount")
    description: Optional[str] = None


class PIXTransfer(BaseModel):
    amount: float
    pix_key: str = Field(..., alias="pixKey")
    e2e_id: str = Field(..., alias="e2eId")


class BilletPayment(BaseModel):
    account_id: str = Field(..., alias="accountId")
    amount: float
    billet_code: str = Field(..., alias="billetCode")
    due_date: str = Field(..., alias="dueDate")


class InternalTransfer(BaseModel):
    source_account_id: str = Field(..., alias="sourceAccountId")
    target_account_id: str = Field(..., alias="targetAccountId")
    amount: float
