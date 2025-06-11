from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Transaction
from pydantic import BaseModel
from datetime import datetime

purchase_router = APIRouter(prefix="/api/purchase")

class PurchaseRequest(BaseModel):
    DATETIME: datetime = None
    EMP_CD: str
    STORE_CD: str
    POS_NO: str
    TOTAL_AMT: int
    TTL_AMT_EX_TAX: int

@purchase_router.post("/")
def create_purchase(purchase: PurchaseRequest, db: Session = Depends(get_db)):
    transaction = Transaction(
        DATETIME=purchase.DATETIME or datetime.utcnow(),
        EMP_CD=purchase.EMP_CD,
        STORE_CD=purchase.STORE_CD,
        POS_NO=purchase.POS_NO,
        TOTAL_AMT=purchase.TOTAL_AMT,
        TTL_AMT_EX_TAX=purchase.TTL_AMT_EX_TAX
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return {
        "TRD_ID": transaction.TRD_ID,
        "DATETIME": transaction.DATETIME
    }