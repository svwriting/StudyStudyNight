# import csv
# import codecs
# import requests
# import io
# import json

# with codecs.open("2020-11-25.csv","r","utf-8") as f:
# 	data=list(csv.reader(f))
# 	print(data)


# r1=requests.get("https://ws.moe.edu.tw/001/Upload/4/relfile/0/4764/e2270c3b-2f9a-458b-b582-c661eb83aeb6.csv")
# f=io.StringIO(r1.text)
# data=list(csv.reader(f))
# for d in data:
# 	print(d[0],d[1])


import csv
import codecs
import requests
import io
import json


# r1=requests.get("https://www.ris.gov.tw/rs-opendata/api/v1/datastore/ODRP057/108")
# data=json.loads(r1.text)
# print(data["responseCode"])
# print(data["responseMessage"])
# print(data["totalPage"])
# for d in data["responseData"]:
# 	print(d["site_id"])

# r1=requests.get("http://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/57/f2a35957-93aa-4d4f-9a64-4aa5dc1bedfd.json")
# data=json.loads(r1.text)
# print(data[0]["區域別"])
# for d in data:
# 	print(d["區域別"])
# i=0
# for p in range(1,5):
# 	r1=requests.get(
# 		"https://udn.com/api/more",
# 		params={
# 			"page":p,
# 			"id":"",
# 			"channelId":"1",
# 			"cate_id":"0",
# 			"type":"breaknews",
# 			"totalRecNo":"7795"
# 		}
# 	)
# 	data=json.loads(r1.text)
# 	for d in data["lists"]:
# 		with codecs.open("udn.txt","a","utf-8") as f:
# 			f.write(d["title"]+"\r\n")
# 		r2=requests.get(d["url"])
# 		i+=1
# 		with codecs.open("udn/"+str(i)+".jpg","wb") as f:
# 			f.write(r2.content)


from bs4 import BeautifulSoup
h={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
	"Cookie":"_ga=GA1.2.350837589.1606273357; _gid=GA1.2.978652670.1606273357; _fbp=fb.1.1606273356904.1141079148; __gads=ID=95cd80cd7acb04cc-225d1d55e3c4000a:T=1606273357:S=ALNI_MYDqEbhL1Wi-DXTcHoNSKKYEMFuqw; cto_bundle=NDRZz19JWVIyOGRjMFhjdGdON3FVVmJCSmFHOSUyQkhQc3NZemNTRThrJTJCMGY2RkxTeFJTOE1hVlVEZmU2NG1Oa0M0bGt0VGVsJTJCZmxpOGs0S0pQcGRGTnQlMkZiNThjclFqVjQ4NzVVOUxsNVpCcktSOWlXc0VWdGJCSTlEYyUyRmJSVENPTnFEYllRbGYlMkY0Z2ZUbEVwdVBlZDI0bVNKOUElM0QlM0Q; dable_uid=43714914.1606273361911; __asc=55f8bd37175fe28070f735fc02c; __auc=55f8bd37175fe28070f735fc02c; __lastv=0; __erEvntUid=noset; meter_1=1; meter_7=1; __eruid=1fe21c5c-4925-01d8-91a3-cc5807710f80; __BWfp=c1606286840335x8938648ae; gliaplayer_ssid=10c4f3e1-2eea-11eb-a10f-6b6895c57846; _gliaplayer_user_info={%22city%22:%22shibuya%20city%22%2C%22uid%22:%2210c62c60-2eea-11eb-a10f-6b6895c57846%22%2C%22country%22:%22TW%22%2C%22region%22:%2213%22%2C%22source%22:%22CF%22%2C%22latlong%22:%2235.661971%2C139.703795%22%2C%22ip%22:%22125.227.38.129%22}; last_click_URL=https://money.udn.com/rank/newest/1001/0/1"
}
r1=requests.get(
	"https://money.udn.com/rank/newest/1001/0/1",headers=h
)
i=0
b=BeautifulSoup(r1.text, "html.parser")
data=b.find_all("td")
for d in data:
	if "class" not in d.attrs:
		data2=d.find("a")
		r2=requests.get(
			data2.attrs["href"],headers=h
		)
		b2=BeautifulSoup(r2.text, "html.parser")
		datetime=b2.find("div",{"class":"shareBar__info--author"}).find("span").text
		content=""
		for d2 in b2.find_all("p"):
			content+=d2.text
		i+=1
		with codecs.open("udn2/"+str(i)+".txt","w","utf8") as f:
			f.write(data2.attrs["href"]+"\r\n")
			f.write(data2.text+"\r\n")
			f.write(datetime+"\r\n\r\n")
			f.write(content)
		try:
			j=0
			for d3 in b2.find_all("figure"):
				r3=requests.get(d3.find("a").attrs["href"],headers=h)
				j+=1
				with codecs.open("udn2/image/"+str(i)+"-"+str(j)+".jpg","wb") as f:
					f.write(r3.content)
		except:
			pass

		


