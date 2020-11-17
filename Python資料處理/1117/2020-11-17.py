import pymysql

link=pymysql.connect(
	host="localhost",
	user="root",
	passwd="",
	db="my",
	charset="utf8",
	port=3306
)

cur=link.cursor()
# x=[
# 	input("Title:"),
# 	input("Description:"),
# 	input("Source:"),
# 	input("Create Time:"),
# 	input("URL:"),
# 	input("Photo URL:"),
# 	input("Keyword:")
# ]
# cur.execute(
# 	"INSERT INTO `news`"+
# 	"(`title`,`description`,`src`,`create_time`,`url`,`photo_url`,`keyword`) "+
# 	"VALUES(%s,%s,%s,%s,%s,%s,%s)",
# 	x
# )
# link.commit()
x={
	"a":input("Title:"),
	"b":input("Description:"),
	"c":input("Source:"),
	"d":input("Create Time:"),
	"e":input("URL:"),
	"f":input("Photo URL:"),
	"g":input("Keyword:")
}
cur.execute(
	"INSERT INTO `news`"+
	"(`title`,`description`,`src`,`create_time`,`url`,`photo_url`,`keyword`) "+
	"VALUES(%(a)s,%(b)s,%(c)s,%(d)s,%(e)s,%(f)s,%(g)s)",
	x
)
link.commit()
print("剛剛新增的資料ID:",cur.lastrowid)

# x={
# 	"c":input("請輸入你要編輯的資料ID:"),
# 	"a":input("Title:"),
# 	"b":input("Description:")
# }
# cur.execute(
# 	"UPDATE `news` SET "+
# 	"`title`=%(a)s,`description`=%(b)s "+
# 	"WHERE `id`=%(c)s",
# 	x
# )
# link.commit()


# x=[input("請輸入你要刪除的資料ID:")]
# cur.execute(
# 	"DELETE FROM `news` WHERE `id`=%s",
# 	x
# )
# link.commit()

# cur.execute("SELECT * FROM `news`")

# d=cur.fetchone()
# print(d[0],d[1])

# d=cur.fetchone()
# print(d[0],d[1])

# d=cur.fetchone()
# print(d[0],d[1])

# for d in cur.fetchall():
# 	print(d[0],d[1])

# print("總共：",cur.rowcount)

link.close()
