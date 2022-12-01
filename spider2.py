import requests

url = 'http://chengyu.wx6.org/category_4zi.aspx'
response = requests.get(url)
print(response.text)