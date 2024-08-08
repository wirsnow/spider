import execjs
import requests

headers = {'Accept': "application/json, text/plain, */*",
           'accessToken': "", 'timeout': '30000', 'v': '231012',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
           }
params = {'itemCode': 'jsbpp_news_bfwjnew', 'pg': '0', 'pgsz': '15'}
res = requests.get('https://jzsc.mohurd.gov.cn/APi/webApi/artcleApi/getPageList', params=params, headers=headers)
data = res.text.replace(' ', '')
with open('mohurd.js', 'r', encoding='utf-8') as f:
    js = f.read()
print(execjs.compile(js).call('b', data))
