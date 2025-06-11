import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルを読み込む

host = os.environ.get("HOST")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
database = os.environ.get("DATABASE")
ssl_ca = os.environ.get("SSL_CA")  
port = int(os.environ.get("PORT", 3306))


conn = mysql.connector.connect(
     host=host,
    user=user,
    password=password,
    database=database,
    port=port,
    ssl_ca=ssl_ca
)

cursor = conn.cursor()

# 既存テーブルを削除して初期化（順序に注意）
cursor.execute("DROP TABLE IF EXISTS 取引明細;")
cursor.execute("DROP TABLE IF EXISTS 取引;")
cursor.execute("DROP TABLE IF EXISTS 商品マスタ;")

# 商品マスタ
cursor.execute("""
CREATE TABLE IF NOT EXISTS 商品マスタ (
    PRD_ID INT PRIMARY KEY AUTO_INCREMENT,
    CODE BIGINT UNIQUE,
    NAME VARCHAR(50),
    PRICE INT
);
""")

# 取引
cursor.execute("""
CREATE TABLE IF NOT EXISTS 取引 (
    TRD_ID INT PRIMARY KEY AUTO_INCREMENT,
    DATETIME TIMESTAMP,
    EMP_CD CHAR(10),
    STORE_CD CHAR(5),
    POS_NO CHAR(3),
    TOTAL_AMT INT,
    TTL_AMT_EX_TAX INT
);
""")

# 取引明細
cursor.execute("""
CREATE TABLE IF NOT EXISTS 取引明細 (
    DETAIL_ID INT PRIMARY KEY AUTO_INCREMENT,
    TRD_ID INT,
    DTL_ID INT,
    PRD_ID INT,
    PRD_CODE CHAR(13),
    PRD_NAME VARCHAR(50),
    PRD_PRICE INT,
    TAX_CD CHAR(2),
    FOREIGN KEY (TRD_ID) REFERENCES 取引(TRD_ID),
    FOREIGN KEY (PRD_ID) REFERENCES 商品マスタ(PRD_ID)
);
""")

conn.commit()
cursor.close()
conn.close()