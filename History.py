import json
import sqlite3

# SQLite3 데이터베이스 연결
conn = sqlite3.connect('History')
cursor = conn.cursor()

# SQL 쿼리를 사용하여 테이블에서 정보 추출
cursor.execute("SELECT u.url, uu.url, v.visit_duration FROM visits v JOIN urls u ON v.url = u.id LEFT JOIN urls uu ON v.from_visit = uu.id")
rows = cursor.fetchall()

# 추출된 정보를 Python 사전으로 변환
data = []
for row in rows:
    data.append({
        'url': row[0],
        'url_pre': row[1],
        'time' : row[2]
    })

# JSON 파일로 저장
with open('History.json', 'w') as f:
    json.dump(data, f, indent=4)

# 연결 종료
conn.close()