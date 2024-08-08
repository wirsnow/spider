import urllib.parse as up
data = """itemCode=jsbpp_news_bfwjnew&pg=0&pgsz=15"""

print(up.parse_qs(data))
