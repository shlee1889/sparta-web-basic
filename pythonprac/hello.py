import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# .: 메소드 ['key']: 딕셔너리 벨류
# url에 직접적으로 요청하는 것이 아니라 headers라는 조건을 걸어서 간접적으로 요청함
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

# for tr in trs:
#   img_tag = tr.select_one('td.ac > img')
#   a_tag = tr.select_one('td.title > div > a')
#   point_class = tr.select_one('td.point')
#   if img_tag is not None and a_tag is not None and point_class:
#     rank = img_tag['alt']
#     title = a_tag.text
#     point = point_class.text
#     print(rank + " " + title + " " + point)

# 리팩토링
for tr in trs:
  a_tag = tr.select_one('td.title > div > a')
  if a_tag is not None:
    rank = tr.select_one('td.ac > img')['alt']
    title = a_tag.text
    star = tr.select_one('td.point').text
    doc = {
      'rank': rank,
      'title': title,
      'star': star,
    }
    db.movies.insert_one(doc)

db.users.delete_many({})