from pydantic import BaseModel, Field
from typing import List, Optional


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
    account_id: str = Field(..., alias="accountId")
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
