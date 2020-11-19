import requests
import prettytable
import os

totalPage_=None
pageI_=1

def clearScreen():
    os.system('cls')
def getProList(keyword_="豬",pageI_=0):
    url_=f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={keyword_}&page={pageI_}&sort=sale/dc"
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
    global totalPage_
    totalPage_=r_.json()['totalPage']
    prods_=r_.json()['prods']
    rows_=[(prod_['name'],prod_['price']) for prod_ in prods_]
    table_=prettytable.PrettyTable(["名稱","價格"],encoding="utf8")
    table_.align["名稱"]='l'
    table_.align["價格"]='l'
    for row_ in rows_:
        table_.add_row(row_)
    return table_
    




keyword_=input("關鍵字：")
t_=getProList(keyword_=keyword_)

while (pageI_>=1 and pageI_<=totalPage_):
    clearScreen()
    print(t_)

    try:
        pageI_=int(input("前往頁碼："))
    except:
        print("輸入的不是數字!")
        os._exit(0)
    t_=getProList(keyword_=keyword_,pageI_=pageI_)
else:
    print("頁碼超過範圍！")
