import requests
from bs4 import BeautifulSoup
# 读取网站中a标签文本
# 发送HTTP请求并获取网页内容
url = 'https://moocstudent.github.io/tools.html'
response = requests.get(url)
html_content = response.text
# print("html_content %d",html_content)

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到特定元素并提取数据
# 这里假设要提取id为'tool-list'的元素中的所有文本
tool_list = soup.find_all('a')
# 提取<a>标签的文本内容
for a_tag in tool_list:
    print(a_tag.get_text(strip=True))
