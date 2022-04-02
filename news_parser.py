import requests
from bs4 import BeautifulSoup
import time as tm
from datetime import datetime

text1 = ""
time_pattern = '%a, %d %b %Y %H:%M:%S GMT'
new_time = '2022-04-01 00:25:00'
while True:
  r = requests.get('https://ru.tradingview.com/news/', headers={'Cache-Control': 'no-cache'})
  soup = BeautifulSoup(r.content, "html.parser")
  news = soup.find_all("article", class_="card-exterior-py0Z6Vne article-Ckx7QVGw card-wSNJR2eq")
  news2 = soup.find_all("a", class_="card-wSNJR2eq cardLink-wSNJR2eq")
  
  times = datetime.strptime(news[0].find("time")['datetime'],time_pattern)
  times2 = datetime.strptime(news2[0].find("time")['datetime'],time_pattern)
  
  temp_param = news[0].find("span", class_="title-Ckx7QVGw").text
  temp_param2 = news2[0].find("span", class_="title-Ckx7QVGw").text
  
  for index in range(1, len(news)):
    temp_new_time = news[index].find("time")['datetime']
    temp_new_time = datetime.strptime(temp_new_time, time_pattern)
    if times < temp_new_time:
      times = datetime.strptime(news[index].find("time")['datetime'], time_pattern)
      temp_param = news[index].find("span", class_="title-Ckx7QVGw").text 

  for index in range(1, len(news2)):
    temp_new_time = news2[index].find("time")['datetime']
    temp_new_time = datetime.strptime(temp_new_time, time_pattern)
    if times2 < temp_new_time:
      times2 = datetime.strptime(news[index].find("time")['datetime'], time_pattern)
      temp_param2 = news2[index].find("span", class_="title-Ckx7QVGw").text 

  if times < times2:
    times = times2
    temp_param = temp_param2
      
  if (text1 != temp_param) and (new_time != times):
    text1 = temp_param
    new_time = times
    print(f"Название: {text1}")
    print(f"Опубликовано: {times}")
    tm.sleep(5)
  else:
    tm.sleep(5)
    continue