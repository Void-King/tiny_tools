import requests
import sys
import os
import json
import re
import tkinter as tk
from bs4 import BeautifulSoup
# pip install BeautifulSoup4 -i https://pypi.tuna.tsinghua.edu.cn/simple
def getPic(url):
    proxy = {
        'http': 'http://127.0.0.1:1080',
        'https': 'https://127.0.0.1:1080',
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    # url = "https://www.instagram.com/p/12By4D1AN3Fc4hV/"
    # url = input('输入instagram地址：')
    name = re.findall('[A-z0-9_-]+', url)
    name = name[5]
    print (name)
    res = requests.get(url, headers=headers, proxies=proxy)
    webCon = res.content
    soup = BeautifulSoup(webCon, "html.parser")
    stra = soup.find('meta', attrs={'property': 'og:image'})
    strb = stra['content']
    resPic = requests.get(strb, headers=headers, proxies=proxy)
    strc = resPic.content
    # stra = soup.find('div', attrs={'id': 'search-list'})
    # strb = soup.findAll('span', attrs={'id': 'react-root'})
    print (strb)
    with open(sys.path[0] + '\\' + name +'.jpg', 'wb') as f:
        f.write(strc)


root = tk.Tk()
root.title('instagram pic')
frame = tk.Frame(root)
frame.pack(padx = 20, pady = 20)

label = tk.Label(frame, text = '输入instagram网址：')
label.grid(row = 0, column = 0, sticky = tk.W)

ipt = tk.Entry(frame, width = 80)
ipt.grid(row = 1, column = 0)

def download():
    url = ipt.get()
    getPic(url)

conf = tk.Button(frame, text = '下载', command = download)
conf.grid(row = 1, column = 1, padx = 10)
root.mainloop()

# if __name__ == "__main__":
#     getPic()
    # url = "https://www.instagram.com/p/2B2JqTRJBt7k/"
    # name = re.findall('[A-z0-9]+', url)
    # name = name[5]
    # print (name)