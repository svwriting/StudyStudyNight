import time
import os
import colorama

colorama.init(True)
i=0
while True:
	os.system("cls")
	i+=1
	i%=10
	if i>=1 and i<=5:
		print(colorama.Fore.RED+"■")
	elif i==6:
		print("　"+colorama.Fore.YELLOW+"■")
	else:
		print("　　"+colorama.Fore.GREEN+"■")
	print(i)
	time.sleep(1)