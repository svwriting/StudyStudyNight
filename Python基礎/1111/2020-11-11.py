# import sys as p

# # print(sys.argv)
# for d in p.argv:
# 	print("參數:",d)

# from sys import argv

# for d in argv:
# 	print("參數:",d)

# import os

# # os.system("tasklist")

# p=os.popen("tasklist")
# r=p.read()
# if "notepad.exe" in r:
# 	print("現在有開啟記事本")
# else:
# 	print("沒有開啟記事本")

import codecs

# f=codecs.open("1.txt", "a", "utf-8")
# f.write("ABCDEFG")
# f.close()

# f=codecs.open("1.txt", "r", "utf-8")
# d=f.read()
# f.close()

# print(d)

# with codecs.open("1.txt", "r", "utf-8") as f:
# 	d=f.read()
# print(d)

import os
# os.remove("1.txt")
# os.mkdir("xxx")
# os.rmdir("xxx")
# d=os.listdir(".")
# print(d)
# for d in os.listdir("../../"):
# 	print(d)

# for d in os.listdir("hw/"):
# 	print(d)

# for d in os.listdir("../Zoom/../python/"):
# 	print(d)

# print("工作路徑：",os.getcwd())
# os.chdir("../")
# print("工作路徑：",os.getcwd())

# print(os.path.isdir("2020-11-05.py"))

# for d in os.listdir("./"):
# 	if os.path.isdir(d)==True:
# 		print("[資料夾]",end="")
# 	else:
# 		print("[檔案]",end="")
# 	print(d)

# print(os.path.exists("2020-11-11.py"))

# if os.path.exists("1.txt")==True:
# 	os.remove("1.txt")

# print(os.path.basename("C:/Users/user/Documents/python/2020-11-11.py"))
# print(os.path.dirname("C:/Users/user/Documents/python/2020-11-11.py"))

# print(os.path.getsize("C:/Users/user/Documents/python/2020-11-11.py"))
# d=os.path.getsize("hw/Python-程式設計與基礎實用函式.zip")
# r=["位元組","KB","MB","GB"]
# i=0
# while d>=1024:
# 	d/=1024
# 	i+=1
# print(round(d,2),r[i])

# cmd=""
# while cmd!="0":
# 	os.system("cls")
# 	if cmd=="1":
# 		print("列出檔案...")

# 	elif cmd=="2":
# 		print("列出資料夾...")

# 	elif cmd=="3":
# 		print("顯示檔案內容...")


# 	print("工作路徑：",os.getcwd())
# 	print("        (0) 離開程式\n        (1) 列出檔案\n        (2) 列出資料夾\n        (3) 顯示檔案內容\n        (4) 刪除檔案\n        (5) 執行檔案\n        (6) 進入資料夾\n        (7) 刪除資料夾\n        (8) 回上層資料夾")
# 	cmd=input("操作：")

import time

# print("開始")
# time.sleep(3)
# print("結束")

# i=0
# while i<=100:
# 	os.system("cls")
# 	print(i)
# 	i+=1
# 	time.sleep(1)

# print(time.time())
# time.sleep(1)
# print(time.time())
# i=0
# while i<=100:
# 	print(time.time())
# 	i+=1

# while True:
# 	os.system("cls")
# 	print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 	time.sleep(1)

import prettytable

# p=prettytable.PrettyTable(["Id","Title"], encoding="utf-8")
# p.align["Title"]="r"

# p.add_row(["1","AAA"])
# p.add_row(["2","BBB"])
# print(p)

import colorama


colorama.init(True)

# print("ABC")
# print(colorama.Style.BRIGHT+"ABC"+colorama.Style.RESET_ALL+"123")
# print(colorama.Fore.GREEN+"ABC"+colorama.Style.RESET_ALL+"123")
# print(colorama.Back.GREEN+"ABC"+colorama.Style.RESET_ALL+"123")


p=prettytable.PrettyTable(["Id","Title"], encoding="utf-8")
p.align["Title"]="r"

p.add_row(["1",colorama.Fore.GREEN+"AAA"+colorama.Style.RESET_ALL])
p.add_row(["2",colorama.Fore.GREEN+"BBB"+colorama.Style.RESET_ALL])
# print(colorama.Fore.GREEN+str(p))
print(p)