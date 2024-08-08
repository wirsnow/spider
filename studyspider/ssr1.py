import requests,httpx

res = httpx.Client(http2=True).get('https://spa16.scrape.center/')
print(res.text)


