from fastapi import FastAPI  # FastAPIをインポートしてアプリケーションを作成する
from fastapi.middleware.cors import CORSMiddleware  # CORSミドルウェアをインポートしてクロスオリジンリクエストを許可する
from .database import engine  # データベース接続のエンジンをインポートする
from . import models  # SQLAlchemyモデルをインポートする
from .routers import example_router  # ルーターをインポートする（例としてexample_routerを使用）
from .routers.example_router import example_router
from .routers.product_router import product_router
from .routers.purchase_router import purchase_router

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# CORSの設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンからのリクエストを許可
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)

# データベースのテーブルを作成する
models.Base.metadata.create_all(bind=engine)

# ルーターをアプリケーションに追加
app.include_router(example_router)
app.include_router(product_router)
app.include_router(purchase_router)

# アプリケーションのルートエンドポイントを定義
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}  # ルートにアクセスした際のレスポンスを定義