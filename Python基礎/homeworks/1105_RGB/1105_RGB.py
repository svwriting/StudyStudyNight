from colorama import *
import time
import os

color={'red':Back.RED,'green':Back.GREEN,'yellow':Back.YELLOW}
def blink(t,gapN,colorStr):
    os.system('cls')
    for i in range(gapN):
        print('   ',end='')
    print ( color[colorStr]+ "  ")
    print ((t+1)%10)
    time.sleep(1)

init(autoreset=True)
while True:
    for i in range(0,5):
        blink(i,0,'red')
    for i in range(5,6):
        blink(i,1,'yellow')
    for i in range(6,10):
        blink(i,2,'green')