import requests
import prettytable
from bs4 import BeautifulSoup
import html

    
url_=f"https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html?ID=Thu%20Nov%2019%202020%2011:28:04%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93"
headers_={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
params_={}
data_={}
json_={}
r_=requests.get(
    url_,
    headers=headers_,
    params=params_,
    data=data_,
    json=json_
)
r_.encoding="rtf-8"
soup_=BeautifulSoup(r_.text,"html.parser")
citys_=soup_.find_all('tr')
table_=prettytable.PrettyTable(["地區","氣溫"],encoding="utf8")
table_.align['地區']='l'
table_.align['氣溫']='l'
for city_ in citys_:
    table_.add_row((city_.select_one('th').getText(),city_.select_one('span').getText()))
print(table_)