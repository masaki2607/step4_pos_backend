from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base  # BaseクラスをインポートしてSQLAlchemyのモデルを定義するために使用
import datetime

# 商品モデルを定義するクラス
class Product(Base):
    __tablename__ = '商品マスタ'  # データベース内のテーブル名を指定

    PRD_ID = Column(Integer, primary_key=True, index=True)  # プライマリキーとしてのIDカラム
    CODE = Column(String, unique=True, index=True)
    NAME  = Column(String(50), index=True)  # 商品名を格納するカラム
    PRICE  = Column(Integer)  # 商品の価格を格納するカラム

    # 商品と関連する注文を定義するリレーションシップ
    orders = relationship("Order", back_populates="product")

# 注文モデルを定義するクラス
class Order(Base):
    __tablename__ = '取引明細'  # データベース内のテーブル名を指定

    id = Column(Integer, primary_key=True, index=True)  # プライマリキーとしてのIDカラム
    product_id = Column(Integer, ForeignKey('商品マスタ.PRD_ID'))  # 商品IDを外部キーとして指定
    quantity = Column(Integer)  # 注文数量を格納するカラム

    # 注文と関連する商品を定義するリレーションシップ
    product = relationship("Product", back_populates="orders")

# 注文履歴モデルを定義するクラス
class Transaction(Base):
    __tablename__ = '取引'
    TRD_ID = Column(Integer, primary_key=True, index=True)
    DATETIME = Column(DateTime, default=datetime.datetime.utcnow)
    EMP_CD = Column(String)
    STORE_CD = Column(String)
    POS_NO = Column(String)
    TOTAL_AMT = Column(Integer)
    TTL_AMT_EX_TAX = Column(Integer)