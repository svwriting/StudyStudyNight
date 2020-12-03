import requests
import prettytable
from bs4 import BeautifulSoup

r1=requests.get(
	"https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
	params={
		"ID":"Fri Nov 10 2020 09:33:06 GMT+0800 (台北標準時間)"
	}
)
p=prettytable.PrettyTable(["地區","氣溫"], encoding="utf-8")
b=BeautifulSoup(r1.text, "html.parser")
for d in b.find_all("tr"):
	p.add_row([
		d.find("th").text,
		d.find("span").text
	])
print(p)