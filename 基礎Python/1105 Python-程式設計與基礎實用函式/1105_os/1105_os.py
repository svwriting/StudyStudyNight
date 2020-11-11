import os

def PrintAndInput(menu):
    global menuList
    menuList=[]
    for option in menu:
        menuList.append(option)
    for i in range(len(menuList)):
        print(f"        ({i}) {menuList[i]}")
    return int(input("操作："))

def MENU():
    global menu
    menu={"離開程式":EXIT, \
        "列出檔案":ListFile, \
        "列出資料夾":Listdir, \
        "顯示檔案內容":ShowFileDetail, \
        "刪除檔案":DelFile, \
        "執行檔案":ExFile, \
        "進入資料夾":EnterDir, \
        "刪除資料夾":DelDir, \
        "回上層資料夾":BackDir}
    return PrintAndInput(menu)

def EXIT(): #離開程式
    os._exit(0)
    pass

def ListFile(): #列出檔案
    list_=os.listdir(os.getcwd())
    i_=0
    for i in range(len(list_)):
        path_=(os.getcwd()+'\\'+list_[i])
        if os.path.isfile(path_):
            print(f"{i_} {list_[i]}")
            i_+=1
    pass

def Listdir(): #列出資料夾
    list_=os.listdir(os.getcwd())
    i_=0
    for i in range(len(list_)):
        path_=(os.getcwd()+'\\'+list_[i])
        if os.path.isdir(path_):
            print(f"{i_} {list_[i]}")
            i_+=1
    pass

def ShowFileDetail(): #顯示檔案內容
    global menu
    menu={}
    list_=os.listdir(os.getcwd())
    i_=0
    for i in range(len(list_)):
        path_=(os.getcwd()+'\\'+list_[i])
        if  os.path.isfile(path_): # path_.endswith(".txt"):
            menu[list_[i]]=path_
            i_+=1
    INi=PrintAndInput(menu)
    path_=menu[menuList[INi]]
    print("================檔案開始================")
    with open(path_,mode='r',encoding='utf-8') as file_:
        print(file_.read())
    print("================檔案結束================")
    pass

def DelFile(): #刪除檔案
    global menu,menuList
    menu={}
    cwd=os.getcwd()
    list_=os.listdir(cwd)
    i_=0
    for i in range(len(list_)):
        path_=(cwd+'\\'+list_[i])
        if os.path.isfile(path_):
            path_=path_
            menu[list_[i]]=path_
            i_+=1
    INi=PrintAndInput(menu)
    path_=menu[menuList[INi]]
    os.remove(path_)
    pass

def ExFile(): #執行檔案
    global menu,menuList
    menu={}
    cwd=os.getcwd()
    list_=os.listdir(cwd)
    i_=0
    for i in range(len(list_)):
        path_=(cwd+'\\'+list_[i])
        if os.path.isfile(path_):
            path_=path_
            menu[list_[i]]=path_
            i_+=1
    INi=PrintAndInput(menu)
    path_=menu[menuList[INi]]
    os.system("start "+path_)
    pass

def EnterDir(): #進入資料夾
    global menu,menuList
    menu={}
    cwd=os.getcwd()
    list_=os.listdir(cwd)
    i_=0
    for i in range(len(list_)):
        path_=(cwd+'\\'+list_[i])
        if os.path.isdir(path_):
            path_=path_
            menu[list_[i]]=path_
            i_+=1
    INi=PrintAndInput(menu)
    path_=menu[menuList[INi]]
    os.chdir(path_)
    pass

def DelDir(): #刪除資料夾
    global menu,menuList
    menu={}
    cwd=os.getcwd()
    list_=os.listdir(cwd)
    i_=0
    for i in range(len(list_)):
        path_=(cwd+'\\'+list_[i])
        if os.path.isdir(path_):
            path_=path_
            menu[list_[i]]=path_
            i_+=1
    INi=PrintAndInput(menu)
    path_=menu[menuList[INi]]
    os.removedirs(path_)
    pass

def BackDir(): #回上層資料夾
    os.chdir('../')
    pass



os.system('cls')
menu={}
menuList=[]
print("\n工作路徑："+os.getcwd())
INi=MENU()
while True:
    os.system('cls')
    fun_=menu[menuList[INi]]
    fun_()
    #break
    print("\n工作路徑："+os.getcwd())
    INi=MENU()

