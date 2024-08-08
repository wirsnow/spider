from pprint import pprint

headers = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7
Connection: keep-alive
Cookie: navCtgScroll=0; navCtgScroll=0; _lxsdk_cuid=18cd2dd4fb6c8-0403c381909514-4c657b58-1bcab9-18cd2dd4fb6c8; _lxsdk=18cd2dd4fb6c8-0403c381909514-4c657b58-1bcab9-18cd2dd4fb6c8; _hc.v=66e94f14-6b95-e12e-c340-0cf7a296d030.1704344769; WEBDFPID=0v9vz15yv44v556v105292xxy343762y81xw7ww5xu997958y40w3x05-2019704768785-1704344768785QAYCUIEfd79fef3d01d5e9aadc18ccd4d0c95073215; ctu=be75618e4b5fd5ff3344464bd0840037519c1a3fba50f1fb76f8ccb4d8fa1621; s_ViewType=10; ua=%E9%9C%9C%E9%99%8D; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1704371319; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; qruuid=cd72b132-a585-4cdc-ba62-f61b4439a6bd; dplet=3ce2ad8d0946a9387977c900f32135f6; dper=02021c255a6e7bce65819d09ea5993328daae29df138cf71cc514e20b1a3894469bb9f3ce1f488eaeeea69cd8a40784faabb7e74a84518cd7b7f000000005021000087377f172999d04ad1fc724df5f425f19fb85092415bfc2b12ba18cda304a3c1fa80233ec5b9cb80b07e6ba55abae825; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=190b45f4000--f33-b2e%7C%7C10; fspop=test; cy=3; cye=hangzhou
DNT: 1
Host: www.dianping.com
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0
sec-ch-ua: "Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
"""
headers = headers.split('\n')
header, data = [], []
for x in headers:
    if x != '\n' and x != '':
        a, b = x.split(':')[0],"".join(x.split(':')[1:])
        header.append(a)
        b = b[1:] if b[0] == ' ' else b
        data.append(int(b) if x.isdigit() else str(b))
print(dict(zip(header, data)))
