import os

os.system('cls')
for i in range(1,10):
    STR=""
    for j in range(1,10):
        STR+=f"{i}x{j}={i*j}\t"
    print(f"{STR}")