import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")

# 기준점
data = soup.select_one('#contentarea > div.box_type_l > table')
stocks = data.select("tr")

# 1.상단타이틀. csv파일로 저장
f = open('data.csv','w',encoding='utf-8-sig',newline="")
writer = csv.writer(f)
st_list = [ st.text  for st in stocks[0].select("th") ]
writer.writerow(st_list)
# 30개 주식정보를 csv파일로 저장
for stock in stocks:
  sts = stock.select("td")
  if len(sts) <= 1: continue
  sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
  writer.writerow(sto_list) #writerow 리스트타입을 저장

f.close()
