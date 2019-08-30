from bs4 import BeautifulSoup
import requests
url = 'https://www.sina.com.cn/'
r = requests.get(url)
demo = r.content.decode('utf-8')  # 服务器返回响应并编码
soup = BeautifulSoup(demo, 'html.parser')
"""
demo 表示被解析的html格式的内容
html.parser表示解析用的解析器
"""
# print(soup)  # 输出响应的html对象
# print(soup.prettify())  # 使用prettify()格式化显示输出
# print(soup.title)  # 获取html的title标签的信息
# print(soup.a)  # 获取html的a标签的信息(soup.a默认获取第一个a标签，想获取全部就用for循环去遍历)
# print(soup.a.name)   # 获取a标签的名字








    
    