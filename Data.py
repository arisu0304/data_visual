import json

# JSON 파일 열기
with open('Favicons.json', 'r') as f:
    fav = json.load(f)

Favicons = {}

for key, value in fav.items():
    Favicons[key] = value;    
    
# JSON 파일 열기
with open('History.json', 'r') as f:
    his = json.load(f)

# 추출된 정보를 Python 사전으로 변환
for h in his:
    h['url_fav'] = Favicons.get(h['url'],None)

# JSON 파일로 저장
with open('Data.json', 'w') as f:
    json.dump(his, f, indent=4)