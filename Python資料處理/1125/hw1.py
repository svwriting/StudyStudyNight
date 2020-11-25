import requests

r1=requests.get(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
		"action":"action"
	}
)
r1.encoding="utf-8"
print(r1.text)


r1=requests.delete(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
		"action":"action"
	},
	data={
		"id":"id"
	}
)
r1.encoding="utf-8"
print(r1.text)

r1=requests.put(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
		"action":"action"
	},
	data={
		"id":"id",
		"name":"name"
	}
)
r1.encoding="utf-8"
print(r1.text)

r1=requests.patch(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
		"action":"action"
	},
	data={
		"id":"id",
		"name":"name",
		"address":"address"
	}
)
r1.encoding="utf-8"
print(r1.text)


r1=requests.post(
	"http://teaching.bo-yuan.net/test/requests/",
	params={
		"action":"action"
	},
	data={
		"id":"id",
		"name":"name",
		"address":"address"
	}
)
r1.encoding="utf-8"
print(r1.text)