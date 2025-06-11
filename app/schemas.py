from pydantic import BaseModel  # PydanticのBaseModelをインポートし、データバリデーションを行うための基底クラスを提供

# 商品情報を表現するためのPydanticスキーマ
class Item(BaseModel):
    id: int  # 商品のID
    name: str  # 商品名
    description: str  # 商品の説明
    price: float  # 商品の価格
    quantity: int  # 在庫数

# リクエスト用のスキーマ
class ItemCreate(BaseModel):
    name: str  # 商品名
    description: str  # 商品の説明
    price: float  # 商品の価格
    quantity: int  # 在庫数

# レスポンス用のスキーマ
class ItemResponse(Item):
    pass  # Itemスキーマを継承し、レスポンス用のスキーマを定義

# 複数の商品情報を返すためのスキーマ
class ItemList(BaseModel):
    items: list[ItemResponse]  # ItemResponseのリストを持つスキーマ

# エラーレスポンス用のスキーマ
class ErrorResponse(BaseModel):
    detail: str  # エラーメッセージを表現するフィールド