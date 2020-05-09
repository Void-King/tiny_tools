import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as scr
from tkinter import messagebox
import sys
import os
import datetime
import requests
from ftplib import FTP

def ftp_connect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

"""
从ftp服务器下载文件
"""
def download_file(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

"""
从本地上传文件到ftp
"""
def upload_file(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')

    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


def costCalculator():
    root = tk.Tk()
    root.title("Cost Calculator")
    root.geometry("580x521")
    root.resizable(0, 0)

    # 组件定义
    frame = tk.Frame(root)
    frame1 = tk.Frame(frame)
    frame2 = tk.Frame(frame)
    frame3 = tk.Frame(frame)
    scrb = scr.Scrollbar(frame1)
    cost_list = ttk.Treeview(frame1, show = 'headings',
                                height = 20,
                                yscrollcommand = scrb.set)
    label1 = tk.Label(frame2, text = 'Remaining: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry1 = tk.Text(frame2, width = 10, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label21 = tk.Label(frame2,
                        text = ' Add in Cost: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry2 = tk.Entry(frame2, width = 10,
                        font = ("Microsoft YaHei Mono", 10))
    label22 = tk.Label(frame2, text = ' for: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry22 = tk.Entry(frame2, width = 16,
                        font = ("Microsoft YaHei Mono", 10))
    label23 = tk.Label(frame2, text = ' ',
                        font = ("Microsoft YaHei Mono", 10))
    label4 = tk.Label(frame3, text = 'This Week: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry4 = tk.Text(frame3, width = 10, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label31 = tk.Label(frame3,
                        text = '       Select Cost: ',
                        font = ("Microsoft YaHei Mono", 9))
    entry3 = tk.Text(frame3, width = 26, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label32 = tk.Label(frame3, text = ' ',
                        font = ("Microsoft YaHei Mono", 10))
    # 组件功能实现
    cost_list['columns'] = ['Date','Cost','For']
    cost_list.column('Date', width = 240)
    cost_list.column('Cost', width = 140)
    cost_list.column('For', width = 160)
    cost_list.heading('Date', text = 'Date', anchor = 'w')
    cost_list.heading('Cost', text = 'Cost', anchor = 'w')
    cost_list.heading('For', text = 'For', anchor = 'w')
    cost_list.tag_configure('this_week_tag',
                                background = '#8bd9ff',
                                font = ("Microsoft YaHei Mono", 10))
    cost_list.tag_configure('font_un',
                                font = ("Microsoft YaHei Mono", 10))
    def remianF(tcost):
        entry1.config(state = tk.NORMAL)
        ocost = float(entry1.get('1.0','end'))
        tcost += ocost
        entry1.delete('1.0','end')
        entry1.insert(tk.INSERT, round(tcost, 2))
        entry1.config(state = tk.DISABLED)
    def thisWeek(tcost):
        if tcost < 0:
            entry4.config(state = tk.NORMAL)
            ocost = float(entry4.get('1.0','end'))
            tcost += ocost
            entry4.delete('1.0','end')
            entry4.insert(tk.INSERT, round(tcost, 2))
            entry4.config(state = tk.DISABLED)
    # Mon Tue Wed Thu Fri Sat Sun 
    def weekCost():
        entry4.config(state = tk.NORMAL)
        entry4.delete('1.0', 'end')
        entry4.insert(tk.INSERT, 0)
        entry4.config(state = tk.DISABLED)
        this_week = True
        mon_over = True
        time = int (datetime.datetime.now().strftime('%j'))
        weekday = int (datetime.datetime.now().strftime('%w'))
        if weekday == 0:
            weekday = 7
        for item in cost_list.get_children():
            ltime = datetime.datetime.strptime(str(cost_list.item(item, 'values')[0]), '%Y-%m-%d %H:%M:%S  %a')
            ltime = int(ltime.strftime('%j'))
            # 本周一至今天为止
            if time - ltime < weekday:
                cost_list.item(item, tag = 'this_week_tag')
                tcost = float(cost_list.item(item, 'values')[1])
                thisWeek(tcost)
    def inputCost():
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S  %a')
        # Mon Tue Wed Thu Fri Sat Sun 
        tcost = float(entry2.get())
        tfor = entry22.get()
        cost_list.insert('', 0, values = (time, tcost, tfor), tag = 'this_week_tag')
        remianF(tcost)
        thisWeek(tcost)
    def inputkey(event):
        inputCost()
    def deleteCost():
        titem = cost_list.selection()[0]
        tcost = float(cost_list.item(titem, 'values')[1])
        tcost = -tcost
        remianF(tcost)
        # time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry3.delete('1.0','end')
        cost_list.delete(titem)
        weekCost()
    def deletekey(event):
        deleteCost()
    def selectClick(event):
        entry3.config(state = tk.NORMAL)
        titem = cost_list.selection()[0]
        tdate = cost_list.item(titem, 'values')[0]
        # print (tdate)
        entry3.delete('1.0','end')
        entry3.insert(tk.INSERT, tdate)
        entry3.config(state = tk.DISABLED)
    button1 = tk.Button(frame2, text = 'Add in',
                            font = ("Microsoft YaHei Mono", 8), command = inputCost)
    button2 = tk.Button(frame3, text = 'Delete',
                            font = ("Microsoft YaHei Mono", 8), command = deleteCost)

    # 组件打包
    # f1
    cost_list.pack(side = tk.LEFT)
    scrb.pack(side = tk.LEFT, fill = tk.Y)
    frame1.grid(row = 0, column = 0)
    # f2
    label1.grid(row = 0, column = 0)
    entry1.grid(row = 0, column = 1)
    label21.grid(row = 0, column = 2)
    entry2.grid(row = 0, column = 3)
    label22.grid(row = 0, column = 4)
    entry22.grid(row = 0, column = 5)
    label23.grid(row = 0, column = 6)
    button1.grid(row = 0, column = 7)
    frame2.grid(row = 1, column = 0, sticky = 'w', pady = 10)
    # f3
    label4.grid(row = 0, column = 0)
    entry4.grid(row = 0, column = 1)
    label31.grid(row = 0, column = 2, padx = 5)
    entry3.grid(row = 0, column = 3)
    label32.grid(row = 0, column = 4)
    button2.grid(row = 0, column = 5)
    frame3.grid(row = 2, column = 0, sticky = 'w')
    # f
    frame.pack(padx = 10, pady = 12)
    cost_list.bind('<ButtonRelease-1>', selectClick)
    entry2.bind('<Return>', inputkey)
    cost_list.bind('<Delete>', deletekey)
    entry1.insert(tk.INSERT, 0)
    entry1.config(state = tk.DISABLED)
    entry3.config(state = tk.DISABLED)
    scrb.config(command = cost_list.yview)
    
    # 初始化
    download_file(ftp, r"cost.ini", r"./cost_calculator/cost.ini")
    f = open('./cost_calculator/cost.ini', 'r')
    
    relines = f.readlines()
    
    for i in range(len(relines), 0, -3):
        cost_list.insert('', 0, values = (relines[i - 3][::-1][1:][::-1],
                            relines[i - 2][::-1][1:][::-1],
                            relines[i - 1][::-1][1:][::-1]),
                            tag = 'font_un')
        tcost = float(relines[i - 2][::-1][1:][::-1])
        remianF(tcost)

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            lines = ''
            for item in cost_list.get_children():
                lines += cost_list.item(item, 'values')[0] + '\n'
                lines += cost_list.item(item, 'values')[1] + '\n'
                lines += cost_list.item(item, 'values')[2] + '\n'
            f = open('./cost_calculator/cost.ini', 'w')
            f.writelines(lines)
            f.close()
            upload_file(ftp, r"cost.ini", r"./cost_calculator/cost.ini")
            # print (onlineOutput.split("\n"))
            root.destroy()

    weekCost()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    
    root.mainloop()

if __name__ == "__main__":
    ftp = ftp_connect("ftp.3i35.top", "GuardiansAA", "123456")
    # download_file(ftp, r"cost.ini", r"./cost_calculator/cost.ini")
    # upload_file(ftp, r"cost.ini", r"./cost_calculator/cost.ini")
    costCalculator()
