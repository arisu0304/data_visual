import json
import sqlite3

# SQLite3 데이터베이스 연결
conn = sqlite3.connect(r'File\Favicons')
cursor = conn.cursor()

# SQL 쿼리를 사용하여 테이블에서 정보 추출
cursor.execute("SELECT i.page_url, f.url FROM icon_mapping i JOIN favicons f ON i.icon_id = f.id")
rows = cursor.fetchall()

# 추출된 정보를 Python 사전으로 변환
data = {}

for row in rows:
    data[row[0]] = row[1]

# JSON 파일로 저장
with open('Favicons.json', 'w') as f:
    json.dump(data, f, indent=4)

# 연결 종료
conn.close()