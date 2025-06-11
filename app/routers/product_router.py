from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product
from pydantic import BaseModel
from datetime import datetime

product_router = APIRouter(prefix="/api/products")

@product_router.get("/{barcode}")
def get_product(barcode: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.CODE == barcode).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {
        "name": product.NAME,
        "code": product.CODE,
        "price": product.PRICE
    }

class PurchaseRequest(BaseModel):
    DATETIME: datetime = None  # 省略時はサーバー側で自動設定
    EMP_CD: str
    STORE_CD: str
    POS_NO: str
    TOTAL_AMT: int
    TTL_AMT_EX_TAX: int