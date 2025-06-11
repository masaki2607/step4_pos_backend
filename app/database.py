from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load_dotenv()  # .envファイルから環境変数を読み込む

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


# 環境変数から接続情報を取得
user = os.environ.get("USER")  # 例: tech0sql1@rdbs-step4-brazil-south
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
database = os.environ.get("DATABASE")
ssl_ca = os.environ.get("SSL_CA")  # 例: C:/path/to/DigiCertGlobalRootCA.crt.pem

DATABASE_URL = (
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
    f"?ssl_ca={ssl_ca}"
)

engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# from sqlalchemy import create_engine  # SQLAlchemyのcreate_engine関数をインポート
# from sqlalchemy.ext.declarative import declarative_base  # SQLAlchemyの宣言的ベースをインポート
# from sqlalchemy.orm import sessionmaker  # SQLAlchemyのセッションを作成するためのsessionmakerをインポート

# DATABASE_URL = "mysql+pymysql://root:Masaki1549@localhost/POS"  # データベース接続URLを定義

# # SQLAlchemyエンジンを作成
# engine = create_engine(DATABASE_URL)  # 指定したDATABASE_URLを使用してエンジンを作成

# # 宣言的ベースを作成
# Base = declarative_base()  # モデルクラスの基底クラスを作成

# # セッションローカルを作成
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # セッションを管理するためのローカルセッションを作成

# # データベース接続を取得するための依存関係
# def get_db():  # データベースセッションを取得する関数
#     db = SessionLocal()  # 新しいセッションを作成
#     try:
#         yield db  # セッションを返す
#     finally:
#         db.close()  # セッションを閉じる