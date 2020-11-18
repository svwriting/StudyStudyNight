import  requests

url="http://teaching.bo-yuan.net/test/requests/"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
params={}
data={}
json={}
r_=requests.get(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)

params={"action":"FUCK YOU"}
r_=requests.get(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)

r_=requests.delete(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)

data={"id":"IIIIIIDDDDDD"}
r_=requests.delete(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)

r_=requests.put(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)

data["name"]="Harry Potter"
r_=requests.put(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)

r_=requests.patch(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)

data["address"]="天龍國"
r_=requests.patch(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)

r_=requests.post(
    url,
    headers=headers,
    params=params,
    data=data,
    json=json
)
r_.encoding="rtf-8"
print(r_.text)