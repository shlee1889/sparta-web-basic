import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# url에 직접적으로 요청하는 것이 아니라 headers라는 조건을 걸어서 간접적으로 요청함
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
  # 순위
  span = tr.select_one('td.number').span.extract()
  rank = tr.select_one('td.number').text.rstrip()

  # 제목 #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
  title = tr.select_one('td.info > a.title.ellipsis').text.lstrip()
  
  # 가수 #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
  singer = tr.select_one('td.info > a.artist.ellipsis').text
  
  print(rank, title, singer)
  