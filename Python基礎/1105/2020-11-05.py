# q=10
# # q=q+99
# q+=99
# print("q變數的內容是:",q)
# print("q-5變數的內容是:",q-5)
# print("q*5變數的內容是:",q*5)
# print("q除以5:",q/5)
# print("q除以5的餘數:",q%5)

# x="10"
# y="20"
# print(x+y)

# x=10
# y=20
# print(x+y)

# print("ABC\nDEFG")
# print("\tABC")
# print("\tEFG")

# print("ABC",end="")
# print("DEF")

# x="ABCDEFG"
# z=x.find("E")
# print(z)

# print("abcdefg".find("d"))

# print("101025101124".count("10"))

# print("101025101124".replace("10","*"))
# x="ABCDEFG"
# print(x[3])
# print(x[0:3])
# print(x[-3:])
# print(x[:5])

# x=[1,2,3,"A","B","C",[9,8,7]]
# print(x)
# print(x[0]+5)
# print(x[3]+"XYZ")
# print(x[-1][0])
# z=x[0:4]
# print(z[-1])
# print("x的長度:",len(x))
# print("z的長度:",len(z))
# x=[1,2,3]
# y=["A","B","C"]
# print(x+y)
# print(y+x)

# x+=[4]
# x+=[5]
# print(x)

# x=[1,2,3]
# print(x)
# print(x*2)
# print(x*3)

# x=[1,2,3,1,2,3]
# print(x.index(2))
# print(x.count(2))

# x={
# 	"a":123,
# 	"b":"XYZ",
# 	"c":[9,8,7]
# }
# print(x["b"])
# print(x["c"][1])
# x["b"]="ABC"
# print(x["b"])

# x={
# 	"a":123,
# 	"b":"XYZ",
# 	"c":[9,8,7]
# }
# k=list(x.keys())
# print(k)

# v=list(x.values())
# print(v)

# def test(a,b):
# 	z=a*b
# 	return z
# print(test(5,7))
# print(test(4,3))

# def test(a,b):
# 	z=a*b
# 	x=a/b
# 	return z,x

# q,w=test(5,7)
# print(q)
# print(w)
# print(z)
# y=100

# def test(a=5,b=3):
# 	global y
# 	z=a*b
# 	x=a/b
# 	return z,x
# q,w=test(b=5,a=10)
# print(q)
# print(w)

# x=10
# if x<10:
# 	print("A")
# elif x>10:
# 	print("B")
# elif x!=10:
# 	print("C")
# elif x==10:
# 	print("D")
# else:
# 	print("E")

# x="ABCDEFG"
# if "Z" in x:
# 	print("A")
# else:
# 	print("B")


# x=["A0","B0","C0","D0","E0","F0","G0"]
# if "B" in x:
# 	print("A")
# else:
# 	print("B")

# x={
# 	"a":123,
# 	"b":"XYZ",
# 	"c":[9,8,7]
# }
# if "c" in x:
# 	print("A")
# else:
# 	print("B")

# for x in ["A","B","C"]:
# 	print(x)
# v=0
# for x in [1,2,3,4,5,6,7,8,9,10]:
# 	v+=x
# print(v)
# v=0
# for i in range(1,1001,1):
# 	v+=i
# print(v)
# i=0
# v=0
# while i<1000:
# 	i+=1
# 	v+=i
# print(v)

# i=0
# v=0
# while i<1001:
# 	v+=i
# 	i+=1
# print(v)

# i=0
# v=0
# while i<1000:
# 	i+=1
# 	if i==500:
# 		break
# 	v+=i
# print("i=",i)
# print("v=",v)
# i=0
# v=0
# while i<1000:
# 	i+=1
# 	if i==500:
# 		continue
# 	v+=i
# print("i=",i)
# print("v=",v)

# def test(a):
# 	try:
# 		return a/10
# 	except:
# 		return "參數錯誤"

# print(test(100))
# print(test("ABC"))

class aa:
	x=10
	def __init__(self,v):
		print(self.x+v)
	# @staticmethod
	def test(self,v):
		return v

# class bb:
# 	x=20
# 	@classmethod
# 	def test(cls,v):
# 		return cls.x+v

# print(aa.test(10))

# a=aa(10)
# print(a.test(10))
# b=bb()
# bb.x=30
# print(b.test(20))
# print(bb.test(20))

# while True:
# 	x=input("請輸入：")
# 	if x=="A":
# 		print("你好")
# 	elif x=="B":
# 		print("哈囉")
# 	elif x=="C":
# 		print("哈哈")
# 	else:
# 		print("你輸入甚麼")

# x=input("請輸入X：")
# y=input("請輸入Y：")
# print("X+Y=",int(x)+int(y))

# x=input("請輸入日期：")
# d=x.split("-")
# print(d[0],"年")
# print(d[1],"月")
# print(d[2],"日")
x=[
	input("年："),
	input("月："),
	input("日：")
]
print("-".join(x))