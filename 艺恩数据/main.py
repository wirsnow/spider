import requests
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

url = 'https://www.endata.com.cn/API/GetData.ashx'
data = {'MethodName': 'BoxOffice_GetYearInfoData', 'year': '2024'}
headers = {'Accept': 'text/plain, */*; q=0.01',
           'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'Host': 'www.endata.com.cn',
           'Origin': 'https//www.endata.com.cn',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 '
                         'Edg/126.0.0.0',
           'X-Requested-With': 'XMLHttpRequest'
           }
res = requests.post(url=url, headers=headers, data=data)
data = res.text


def m(data):
    aaa = int(data[-1], 16) + 9
    bbb = int(data[aaa], 16)
    data = fun(data, aaa, 1)
    aaa = data[bbb:bbb + 8]
    data = fun(data, bbb, 8)
    bbb = aaa.encode('utf-8')

    cipher = DES.new(bbb, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(bytes.fromhex(data))

    try:
        decrypted_str = unpad(decrypted_data, DES.block_size).decode('utf-8')
    except ValueError:
        decrypted_str = decrypted_data.decode('utf-8')

    return decrypted_str[:decrypted_str.rfind("}") + 1]


def fun(a, b, c):
    if b == 0:
        return a[c:]
    d = a[:b]
    return d + a[b + c:]


print(m(data))
