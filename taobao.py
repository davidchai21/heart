# coding=utf-8

import sys
import subprocess
import webbrowser

keywords = sys.argv[1:]

url = "https://s.taobao.com/search?q="
for i in keywords:
	url += i + "+"
url = url[:-1] 
# subprocess.call(["open",url])
webbrowser.open_new(url)

