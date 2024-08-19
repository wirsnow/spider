from pprint import pprint

headers = """
accept:application/json
accept-encoding:gzip, deflate, br, zstd
accept-language:zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7
authorization:C4C679329150AC11073DDD3F41A2763067583001E8FB61E09317D2389AD869BA97D9CD2CB39A91571E2EA8D692F226B3
commander-fe-version:2.6.1
content-length:37917300
content-type:multipart/form-data; boundary=----WebKitFormBoundary2g26RoiU3SOhziza
cookie:acw_tc=0b3283ba17235116840811567e1ad3a5f1436680efb9d87b16ca7c7039b9e9; s9g3EiCpPofasTDCJ3mCbGpM6fKjr4ys_USER_TOKEN=C4C679329150AC11073DDD3F41A2763067583001E8FB61E09317D2389AD869BA97D9CD2CB39A91571E2EA8D692F226B3; qbi_ticket=110994; JSESSIONID=1F67B7F8D9F61B891FE29D18AFAAB3D0
dnt:1
origin:https://z-commander.ai-indeed.com
priority:u=1, i
referer:https://z-commander.ai-indeed.com/
sec-ch-ua:"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"
sec-ch-ua-mobile:?0
sec-ch-ua-platform:"Windows"
sec-fetch-dest:empty
sec-fetch-mode:cors
sec-fetch-site:same-origin
uselang:zh-CN
user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0
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
