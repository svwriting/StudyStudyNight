import requests
import prettytable
import os
keyword=input("關鍵字:")
page="1"
while True:
	os.system("cls")
	r1=requests.get(
		"https://ecshweb.pchome.com.tw/search/v3.3/all/results",
		params={
			"q":keyword,
			"page":page,
			"sort":"sale/dc"
		}
	)
	p=prettytable.PrettyTable(["商品名稱","價格"], encoding="utf-8")
	p.align["商品名稱"]="l"
	p.align["價格"]="l"
	data=r1.json()
	for d in data["prods"]:
		p.add_row([d["name"],d["price"]])
	print(p)
	page=input("前往頁碼：")