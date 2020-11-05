import sys
import webbrowser

if len(sys.argv)!=2:
    print("請輸入網址！")
else:
    url=sys.argv[1]
    webbrowser.open(url)