############## import ################
import os
import pymysql
#from pymysql import connect, connections
import prettytable

############## global ################
MENUmap_={}         # 拿來放選單(選項:功能)
password_=None      # 拿來放root密碼
port_=None          # 拿來放連線埠號
connection_=None    # 拿來放資料庫連線
cursor_=None        # 拿來放資料庫游標

##############  func  ################
def generateCursor(connection_):                   # DBoperate 生成資料庫游標
    return connection_.cursor()
def generateConnection(password_,port_):           # DBoperate 生成資料庫連線
    return pymysql.connect(                        #-建立連線並回傳
        host="localhost",                          #-主機名稱
        user="root",                               #-帳號
        password=password_,                        #-密碼
        db="python_ai",                            #-資料庫名稱
        charset="utf8",                            #-編碼
        port=3306 if port_=='' else int(port_)     #-連線端口
    )
    pass

def clearScreen():                                 # UI 清屏
    os.system('cls')
    pass
def print_menu_get_cmd_do_func():                  # UI 列出選單+接收指令+執行動作
    global MENUmap_
    temp_=enumerate(MENUmap_)                      #-根據MENUmap_生成 索引:key
    for list_i,list_title in enumerate(MENUmap_):
        print(f"({list_i}) {list_title}")          #-一一列出選單內的選項，格式為 "(索引) 選項"
    temp_=dict(temp_)                              #-把enumerate轉成dictionary
    CMD_=input("指令：")                           #-接收指令
    try:                                           #-懶人處理法try/catch，避免錯誤的操作輸入
        MENUmap_[temp_[int(CMD_)]]()               #-根據指令(索引)取出key,根據key取出應執行的func
    except:
        clearScreen()
    pass
def toTopMENU():                                   # UI 走主選單
    global MENUmap_
    MENUmap_={
        "離開程式":toEXIT,
        "顯示會員列表":toShowMemberList,
        "新增會員資料":toInsertNewMember,
        "更新會員資料":toUpdateMemberData,
        "刪除會員資料":toDeleteAMember
    }
    print_menu_get_cmd_do_func()
    pass

def toEXIT():                                      # func 離開程式
    clearScreen()                                  #-清屏
    global connection_
    connection_.close()                            #-關閉連線
    os._exit(0)                                    #-結束程式
    pass
def toShowMemberList():                            # func 顯示會員列表
    clearScreen()                                  #-清屏
    global cursor_
    cursor_.execute(
        "SELECT * FROM `member` ORDER BY `id` ASC" #-SELECT指令
    )
    table_=prettytable.PrettyTable(                #-美麗的表(直譯)
        ["編號","姓名","生日","地址"], 
        encoding="utf8"
    )
    for row_ in cursor_.fetchall():
        table_.add_row(
            [row_[0],row_[1],row_[2],row_[3]]      #-裝填表格
        )
    print(table_)
    pass
def toInsertNewMember():                           # func 新增會員資料
    clearScreen()                                  #-清屏
    global cursor_
    global connection_
    member_={                                      #-準備新增的會員資料
        '`name`':input("請輸入會員姓名："),
        '`birthday`':input("請輸入會員生日："),
        '`address`':input("請輸入會員地址：")
    }
    member_keys=','.join(member_.keys())           #-用','串起keys (等於欄位，這裡只是試試跟老師不同的做法)
    member_values=','.join(
        [ f"'{val_}'" for val_ in member_.values()]#-差不多的原理產生VAULES，一樣純粹玩玩不同方式
    )
    cursor_.execute(                               #-INsert指令，懶得打欄位+順便試試不同玩法
        "INSERT INTO `member` (%s) VALUES (%s)" \
                    % (member_keys, member_values)
    )
    connection_.commit()                           #-commit
    clearScreen()                                  #-清屏
    pass
def toUpdateMemberData():                          # func 更新會員資料
    toShowMemberList()                             #-顯示會員列表
    global cursor_
    global connection_
    member_={                                      #-準備更新的會員資料
        'id':input("請選擇要修改的資料編號："),
        'name':input("請輸入會員姓名："),
        'birthday':input("請輸入會員生日："),
        'address':input("請輸入會員地址：")
    }
    cursor_.execute(                               #-UPDATE指令，想不到什麼好方法偷懶
        "UPDATE `member` SET `name`=%(name)s,`birthday`=%(birthday)s,`address`=%(address)s WHERE `id`=%(id)s" \
                    , member_)
    connection_.commit()                           #-commit
    clearScreen()                                  #-清屏
    pass
def toDeleteAMember():                             # func 刪除會員資料
    toShowMemberList()                             #-顯示會員列表
    global cursor_
    global connection_
    member_id=input("請選擇要刪除的資料編號：")     #-要刪除的資料編號
    cursor_.execute(                               #-DELETE指令
        "DELETE FROM `member` WHERE `id`=%s" \
            % member_id)
    connection_.commit()                           #-commit
    clearScreen()                                  #-清屏
    pass

##############  main  ################
password_=input("請輸入資料庫root密碼：")           #取得密碼
port_=input("請輸入資料庫的port：")                 #取得埠號
try:   #我就是懶-try
    connection_=generateConnection(password_,port_)#建立連線
except:#我就是懶-except
    clearScreen()                                  #讓我們當作什麼都沒發生過
    os._exit(0)
cursor_=generateCursor(connection_)                #建立游標

clearScreen()                                      #清屏
while True:                                        #一直跑一直跑一直跑
    toTopMENU()                                    #跑主選單

### 下面這行其實執行不到， ############
### 真正關閉連線我在 toExit() 裡做 ####
connection_.close()                                #關閉連線
######################################
