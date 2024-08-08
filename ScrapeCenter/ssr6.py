import base64
import hashlib
import time

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.'
}

arg = '/api/movie'
t = str(int(time.time()))
temp = hashlib.sha1(','.join([arg, t]).encode()).hexdigest()
token = base64.b64encode(','.join([temp, t]).encode()).decode()

limit = 110
offset = 0
home_api_url = f'https://spa6.scrape.center/api/movie/?limit={limit}&offset={offset}&token={token}'
request = requests.get(home_api_url)
data = request.json()
for id in data['results']:
    detail = 'ef34#teuq0btua#(-57w1q5o5--j@98xygimlyfxs*-!i-0-mb' + str(id['id'])
    detail = base64.b64encode(detail.encode()).decode()

    token = f'/api/movie/{detail}'
    t = str(int(time.time()))
    temp = hashlib.sha1(','.join([token, t]).encode()).hexdigest()
    token = base64.b64encode(','.join([temp, t]).encode()).decode()

    detail_api_url = f'https://spa6.scrape.center/api/movie/{detail}/?token={token}'
    request = requests.get(detail_api_url)
    data = request.json()
    # 一条就够了
    print(data)
    break
