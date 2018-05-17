'''
爬取豆瓣标签li的值
'''
import requests
import bs4
index_url = 'https://www.douban.com'
def get_video_page_urls():
    response = requests.get(index_url)
    soup = bs4.BeautifulSoup(response.text,'lxml')
    return [a.text for a in soup.select('div#anony-nav div.anony-nav-links ul li')]

# for i in get_video_page_urls():
#  print(i)
print(get_video_page_urls())