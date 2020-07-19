import random
import requests
import xml.etree.ElementTree as ET
from lxml import etree
from requests_html import HTMLSession
from bs4 import BeautifulSoup

URL = input('input the poster URL : ')
# test URL = 'https://www.instagram.com/p/CCxf8G-CiPB/?utm_source=ig_web_copy_link'

# random header(not necessary)
headers_list = ["User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0","User-Agent:Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)","User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)","Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1","Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11","Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)","Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)","Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)","Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)"]
ua_agent = random.choice(headers_list)
headers = {"User-Agent": ua_agent}

# using session to get processed data bt JS
response = HTMLSession().get(URL, headers=headers)
response.html.render(sleep=1, scrolldown=1, wait=0.2)

# get the web content
poster = etree.HTML(response.html.html)

# xpath :
# /html/body/div[1]/section/main/div/div/article/div[2]/div/div/div[1]/img

img_part = poster.xpath('/html/body/div[1]/section/main/div/div/article/div[2]/div/div/div[1]/img')

# claim a BS to get the <img> tag and take attribute "src"
print(str(ET.tostring(img_part[0], encoding='utf8')))
x = BeautifulSoup(str(ET.tostring(img_part[0], encoding='utf8')), 'html.parser')
img_tag = x.find_all('img')
print(img_tag[0].get('src'))

# go and get the picture by "src", so i make a request.
pic_web = requests.get(img_tag[0].get('src'))
pic_web_content = pic_web.content

# save it to folder "imglib" which is under the project folder "web_crawler"
pic_name = input("input the picture name : ")
pic_out = open("./imglib/" + pic_name + ".jpg", 'wb')
pic_out.write(pic_web_content)
pic_out.close()

print('downloaded')
