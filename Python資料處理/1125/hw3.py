import pymysql
import os
import prettytable

os.system("cls")
passwd=input("請輸入資料庫root密碼：")
port=input("請輸入資料庫的Port：")
if port=="":
	port="3306"

link=pymysql.connect(
	host="localhost",
	user="root",
	passwd=passwd,
	db="python_ai",
	charset="utf8",
	port=int(port)
)
cur=link.cursor()
cmd=""
while cmd!="0":
	os.system("cls")
	if cmd in ("1","3","4","5","6"):
		t=prettytable.PrettyTable(["編號","姓名","生日","地址","電話"], encoding="utf8")
		t.align["編號"]="l"
		t.align["姓名"]="l"
		t.align["生日"]="l"
		t.align["地址"]="l"
		t.align["電話"]="l"
		cur.execute("SELECT `m`.*,`t`.`tel` FROM `member` AS `m` LEFT JOIN `tel` AS `t` ON `m`.`id`=`t`.`member_id` ORDER BY `m`.`id` ASC")
		data=cur.fetchall()
		for i in range(0,len(data),1):
			if i==0 or data[i][0]!=data[i-1][0]:
				t.add_row(data[i])
			else:
				t.add_row(["","","","",data[i][4]])
		print(t)

	if cmd=="2":
		param=[
			input("請輸入會員姓名："),
			input("請輸入會員生日："),
			input("請輸入會員地址：")
		]
		cur.execute("INSERT INTO `member`(`name`,`birthday`,`address`) VALUES(%s,%s,%s)",param)
		link.commit()
		os.system("cls")
	elif cmd=="3":
		i=input("請選擇你要修改的資料編號：")
		param=[
			input("請輸入會員姓名："),
			input("請輸入會員生日："),
			input("請輸入會員地址："),
			i
		]
		cur.execute("UPDATE `member` SET `name`=%s,`birthday`=%s,`address`=%s WHERE `id`=%s",param)
		link.commit()
		os.system("cls")
	elif cmd=="4":
		cur.execute("DELETE FROM `member` WHERE `id`=%s",[input("請選擇你要刪除的資料編號：")])
		link.commit()
		os.system("cls")
	elif cmd=="5":
		param=[
			input("請選擇要添加電話的會員編號："),
			input("請輸入電話：")
		]
		cur.execute("INSERT INTO `tel`(`member_id`,`tel`) VALUES(%s,%s)",param)
		link.commit()
		os.system("cls")
	elif cmd=="6":
		cur.execute("SELECT `id`,`tel` FROM `tel` WHERE `member_id`=%s",[
			input("請選擇要刪除電話的會員編號：")
		])
		t=prettytable.PrettyTable(["編號","電話"], encoding="utf8")
		t.align["編號"]="l"
		t.align["電話"]="l"
		for d in cur.fetchall():
			t.add_row(d)
		print(t)
		cur.execute("DELETE FROM `tel` WHERE `id`=%s",[input("請輸入要刪除的電話編號：")])
		link.commit()
		os.system("cls")

	print("(0) 離開程式\n(1) 顯示會員列表\n(2) 新增會員資料\n(3) 更新會員資料\n(4) 刪除會員資料\n(5) 新增會員的電話\n(6) 刪除會員的電話")
	cmd=input("指令：")

link.close()