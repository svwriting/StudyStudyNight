import os
import codecs
cmd=""
while cmd!="0":
	os.system("cls")
	fileList=[]
	dirList=[]
	for d in os.listdir("./"):
		if os.path.isdir(d)==True:
			dirList+=[d]
		else:
			fileList+=[d]

	if cmd in ("1","3","4","5"):
		for i in range(0,len(fileList)):
			print(i,fileList[i])
		print("")
	elif cmd in ("2","6","7"):
		for i in range(0,len(dirList)):
			print(i,dirList[i])
		print("")

	if cmd=="3":
		i=int(input("請輸入檔案索引："))
		os.system("cls")
		with codecs.open(fileList[i], "r", "utf-8") as f:
			print("================檔案開始================")
			print(f.read())
			print("================檔案結束================")
	elif cmd=="4":
		i=int(input("請輸入檔案索引："))
		os.remove(fileList[i])
		os.system("cls")
	elif cmd=="5":
		i=int(input("請輸入檔案索引："))
		os.system("cls")
		os.system(fileList[i])
	elif cmd=="6":
		i=int(input("請輸入資料夾索引："))
		os.chdir(os.getcwd()+"/"+dirList[i])
		os.system("cls")
	elif cmd=="7":
		i=int(input("請輸入資料夾索引："))
		os.rmdir(dirList[i])
		os.system("cls")
	elif cmd=="8":
		os.chdir(os.path.dirname(os.getcwd()))

	print("工作路徑：",os.getcwd())
	print("        (0) 離開程式\n        (1) 列出檔案\n        (2) 列出資料夾\n        (3) 顯示檔案內容\n        (4) 刪除檔案\n        (5) 執行檔案\n        (6) 進入資料夾\n        (7) 刪除資料夾\n        (8) 回上層資料夾")
	cmd=input("操作：")
