import os
import sys
import tkinter as tk

root = tk.Tk()
root.title('weibo pic')
frame = tk.Frame(root)
frame.pack(padx = 20, pady = 30)

label = tk.Label(frame, text = '输入微博昵称：')
label.grid(row = 0, column = 0, sticky = tk.W)

ipt = tk.Entry(frame, width = 30)
ipt.grid(row = 1, column = 0)

def download():
    name = ipt.get()
    cmd = 'cd ' + sys.path[0] + '& start cmd /k python weibo_download.py -u ' + name
    os.system(cmd)

conf = tk.Button(frame, text = '下载', command = download)
conf.grid(row = 1, column = 1, padx = 10)
root.mainloop()
# name = input('输入微博昵称：\n')
# cmd = 'cd ' + sys.path[0] + '& start cmd /k python weibo_download.py -u ' + name
# os.system(cmd)