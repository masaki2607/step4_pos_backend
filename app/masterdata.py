import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む

# 環境変数から接続情報を取得
host = os.environ.get("HOST")
user = os.environ.get("USER")  # 例: tech0sql1@rdbs-step4-brazil-south
password = os.environ.get("PASSWORD")
database = os.environ.get("DATABASE")
ssl_ca = os.environ.get("SSL_CA")  # 例: C:\path\to\DigiCertGlobalRootCA.crt.pem

# MySQL に接続
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    ssl_ca=ssl_ca
)

cursor = conn.cursor()

# データを挿入するSQL文
sql = """
INSERT INTO 商品マスタ (PRD_ID, CODE, NAME, PRICE)
VALUES (%s, %s, %s, %s)
"""

# 挿入したいデータ（タプル）
data_list = [
    (1, 4901681349715, "フィラーレef 0.5/P-BAS86-BK/軸色・ブラック/インキ色・黒", 1650),
    (2, 4901681349784, "フィラーレef 0.5/P-BAS86-WR/軸色・ワイン/インキ色・黒", 1650),
    (3, 4901681349791, "フィラーレef 0.5/P-BAS86-BG/軸色・ブルーグリーン/インキ色・黒", 1650),
    (4, 4901681349777, "フィラーレef 0.5/P-BAS86-P/軸色・ピンク/インキ色・黒", 1650),
    (5, 4901681349746, "フィラーレef 0.5/P-BAS86-BE/軸色・ベージュ/インキ色・黒", 1650),
    (6, 4901681349760, "フィラーレef 0.5/P-BAS86-W/軸色・ホワイト/インキ色・黒", 1650),
]

# SQL 実行
for data in data_list:
    cursor.execute(sql, data)

# コミットして保存
conn.commit()
print("データを追加しました。")

# 接続終了
cursor.close()
conn.close()