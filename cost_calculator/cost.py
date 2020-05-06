import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as scr
from tkinter import messagebox
import sys
import os
import datetime

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
    entry2 = tk.Entry(frame2, width = 10)
    label22 = tk.Label(frame2, text = ' for: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry22 = tk.Entry(frame2, width = 16)
    label23 = tk.Label(frame2, text = ' ',
                        font = ("Microsoft YaHei Mono", 10))
    label31 = tk.Label(frame3,
                        text = 'Select Cost: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry3 = tk.Text(frame3, width = 23, height = 1,
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
    def remianF(tcost):
        entry1.config(state = tk.NORMAL)
        ocost = int(entry1.get('1.0','end'))
        tcost += ocost
        entry1.delete('1.0','end')
        entry1.insert(tk.INSERT, tcost)
        entry1.config(state = tk.DISABLED)

    def inputCost():
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tcost = int(entry2.get())
        tfor = entry22.get()
        cost_list.insert('', 0, values = (time, tcost, tfor))
        remianF(tcost)
    def inputkey(event):
        inputCost()
    def deleteCost():
        titem = cost_list.selection()[0]
        tcost = int(cost_list.item(titem, 'values')[1])
        tcost = -tcost
        remianF(tcost)
        # time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry3.delete('1.0','end')
        cost_list.delete(titem)
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
    frame2.grid(row = 1, column = 0, sticky = 'e', pady = 10)
    # f3
    label31.grid(row = 0, column = 0)
    entry3.grid(row = 0, column = 1)
    label32.grid(row = 0, column = 2)
    button2.grid(row = 0, column = 3)
    frame3.grid(row = 2, column = 0, sticky = 'e')
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
    f = open('./cost_calculator/cost.ini', 'r')
    relines = f.readlines()
    for i in range(len(relines), 0, -3):
        cost_list.insert('', 0, values = (relines[i - 3][::-1][1:][::-1],
                            relines[i - 2][::-1][1:][::-1],
                            relines[i - 1][::-1][1:][::-1]))
        remianF(int(relines[i - 2][::-1][1:][::-1]))
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            lines = ''
            for item in cost_list.get_children():
                lines += cost_list.item(item, 'values')[0] + '\n'
                lines += cost_list.item(item, 'values')[1] + '\n'
                lines += cost_list.item(item, 'values')[2] + '\n'
            f = open('./cost_calculator/cost.ini', 'w')
            f.writelines(lines)
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

if __name__ == "__main__":
    costCalculator()
    # cmdCall("pass")
