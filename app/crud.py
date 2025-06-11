from sqlalchemy.orm import Session  # SQLAlchemyのセッションをインポート
from . import models, schemas  # モデルとスキーマをインポート

# 新しいアイテムをデータベースに追加する関数
def create_item(db: Session, item: schemas.ItemCreate):  
    db_item = models.Item(**item.dict())  # スキーマからモデルに変換
    db.add(db_item)  # データベースにアイテムを追加
    db.commit()  # 変更をコミット
    db.refresh(db_item)  # 新しく追加したアイテムを更新
    return db_item  # 追加したアイテムを返す

# データベースから全アイテムを取得する関数
def get_items(db: Session, skip: int = 0, limit: int = 10):  
    return db.query(models.Item).offset(skip).limit(limit).all()  # 指定されたスキップとリミットでアイテムを取得

# IDで特定のアイテムを取得する関数
def get_item(db: Session, item_id: int):  
    return db.query(models.Item).filter(models.Item.id == item_id).first()  # IDでアイテムをフィルタリングして取得

# アイテムを更新する関数
def update_item(db: Session, item_id: int, item: schemas.ItemUpdate):  
    db_item = get_item(db, item_id)  # 更新するアイテムを取得
    if db_item:  # アイテムが存在する場合
        for key, value in item.dict(exclude_unset=True).items():  # 更新するフィールドをループ
            setattr(db_item, key, value)  # アイテムの属性を更新
        db.commit()  # 変更をコミット
        db.refresh(db_item)  # 更新されたアイテムを再取得
    return db_item  # 更新されたアイテムを返す

# アイテムを削除する関数
def delete_item(db: Session, item_id: int):  
    db_item = get_item(db, item_id)  # 削除するアイテムを取得
    if db_item:  # アイテムが存在する場合
        db.delete(db_item)  # アイテムを削除
        db.commit()  # 変更をコミット
    return db_item  # 削除されたアイテムを返す