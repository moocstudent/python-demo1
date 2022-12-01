import socket
import urllib.error
from urllib import request

url = 'http://chengyu.wx6.org/category_4zi.aspx'
# url = 'http://httpbin.org'

headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "zh-CN,zh;q=0.8",
"Connection": "close",
"Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
"Referer": "http://httpbin.org/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

try:
    req = request.Request(url=url,headers=headers,method='GET')
    response = request.urlopen(req)
    print(response)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
