import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as scr
from tkinter import messagebox
import sys
import os
import datetime
import requests
import pymssql

def costCalculator():
    root = tk.Tk()
    root.title("Cost Calculator---Week From Sunday---Month From 20")
    root.geometry("580x553+1000+200")
    root.resizable(0, 0)
    root.iconbitmap("./gold_coin.ico")
    
    eatTypes = ["买菜", "包子", "炸鸡", "零食", "酒", "米", "奶粉", "披萨"]

    # 组件定义
    frame = tk.Frame(root)
    frame1 = tk.Frame(frame)
    frame2 = tk.Frame(frame)
    frame3 = tk.Frame(frame)
    frame4 = tk.Frame(frame)
    scrb = scr.Scrollbar(frame1)
    cost_list = ttk.Treeview(frame1, show = 'headings',
                                height = 20,
                                yscrollcommand = scrb.set)
    label2_1 = tk.Label(frame2, text = 'Remaining: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry2_2 = tk.Text(frame2, width = 10, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label2_3 = tk.Label(frame2,
                        text = ' Add in Cost: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry2_4 = tk.Entry(frame2, width = 10,
                        font = ("Microsoft YaHei Mono", 10))
    label2_5 = tk.Label(frame2, text = ' for: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry2_6 = tk.Entry(frame2, width = 16,
                        font = ("Microsoft YaHei Mono", 10))
    label2_7 = tk.Label(frame2, text = ' ',
                        font = ("Microsoft YaHei Mono", 10))
    # 第二行
    label3_1 = tk.Label(frame3, text = 'Week: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry3_2 = tk.Text(frame3, width = 8, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label3_3 = tk.Label(frame3,
                        text = 'Month: ',
                        font = ("Microsoft YaHei Mono", 9))
    entry3_4 = tk.Text(frame3, width = 8, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label3_5 = tk.Label(frame3,
                        text = ' Select:',
                        font = ("Microsoft YaHei Mono", 9))
    entry3_6 = tk.Text(frame3, width = 26, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label3_7 = tk.Label(frame3, text = ' ',
                        font = ("Microsoft YaHei Mono", 10))
    # 第三行
    label4_1 = tk.Label(frame4, text = 'Week Eat: ',
                        font = ("Microsoft YaHei Mono", 10))
    entry4_2 = tk.Text(frame4, width = 8, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label4_3 = tk.Label(frame4,
                        text = '   Month Eat: ',
                        font = ("Microsoft YaHei Mono", 9))
    entry4_4 = tk.Text(frame4, width = 8, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label4_5 = tk.Label(frame4,
                        text = '   Month Other:',
                        font = ("Microsoft YaHei Mono", 9))
    entry4_6 = tk.Text(frame4, width = 8, height = 1,
                        font = ("Microsoft YaHei Mono", 10))
    label4_7 = tk.Label(frame4, text = ' ',
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
    cost_list.tag_configure('this_month_tag',
                                background = '#cbf9ff',
                                font = ("Microsoft YaHei Mono", 10))
    cost_list.tag_configure('font_un',
                                font = ("Microsoft YaHei Mono", 10))
    def monthCal(time):
        time_str = datetime.datetime.now().strftime('%Y-%m-%d')
        time_now = int(datetime.datetime.now().strftime('%j'))
        monthday = int(datetime.datetime.now().strftime('%d'))
        time = int(time.strftime('%j'))
        # print (time_now - time)
        if monthday >= 20:
            if time_now - time <= monthday - 20:
                return True
            else:
                return False
        else:
            # print (time_str[5:7])
            time_str_m = str(int(time_str[5:7]) - 1)
            if int(time_str[5:7]) - 1 < 10:
                time_str_m = '0' + time_str_m
            time_str_n = time_str[:5] + str(time_str_m) + '-20'
            # print (time_str)
            # print (time_str_n)
            ltime = int(datetime.datetime.strptime(time_str_n,
                        '%Y-%m-%d').strftime('%j'))
            # print (time - ltime)
            if time - ltime >= 0:
                return True
            else:
                return False
    def remianF(tcost):
        entry2_2.config(state = tk.NORMAL)
        ocost = float(entry2_2.get('1.0','end'))
        tcost += ocost
        entry2_2.delete('1.0','end')
        entry2_2.insert(tk.INSERT, round(tcost, 2))
        entry2_2.config(state = tk.DISABLED)
    # add month 2020 05 19
    def thisWeek(tcost, week, month):
        if tcost < 0:
            if week:
                entry3_2.config(state = tk.NORMAL)
                ocost = float(entry3_2.get('1.0','end'))
                ocost += tcost
                entry3_2.delete('1.0','end')
                entry3_2.insert(tk.INSERT, round(ocost, 2))
                entry3_2.config(state = tk.DISABLED)
            if month:
                entry3_4.config(state = tk.NORMAL)
                mcost = float(entry3_4.get('1.0','end'))
                mcost += tcost
                entry3_4.delete('1.0','end')
                entry3_4.insert(tk.INSERT, round(mcost, 2))
                entry3_4.config(state = tk.DISABLED)
    def thisWeekEat(tcost, week, month, eat):
        if tcost < 0:
            if week:
                if eat:
                    entry4_2.config(state = tk.NORMAL)
                    ocost = float(entry4_2.get('1.0','end'))
                    ocost += tcost
                    entry4_2.delete('1.0','end')
                    entry4_2.insert(tk.INSERT, round(ocost, 2))
                    entry4_2.config(state = tk.DISABLED)
            if month:
                if eat:
                    entry4_4.config(state = tk.NORMAL)
                    mcost = float(entry4_4.get('1.0','end'))
                    mcost += tcost
                    entry4_4.delete('1.0','end')
                    entry4_4.insert(tk.INSERT, round(mcost, 2))
                    entry4_4.config(state = tk.DISABLED)
                else:
                    entry4_6.config(state = tk.NORMAL)
                    mcost = float(entry4_6.get('1.0','end'))
                    mcost += tcost
                    entry4_6.delete('1.0','end')
                    entry4_6.insert(tk.INSERT, round(mcost, 2))
                    entry4_6.config(state = tk.DISABLED)
    # Mon Tue Wed Thu Fri Sat Sun 
    # add month 2020 05 19
    def weekCost():
        entry3_2.config(state = tk.NORMAL)
        entry3_2.delete('1.0', 'end')
        entry3_2.insert(tk.INSERT, 0)
        entry3_2.config(state = tk.DISABLED)
        
        entry4_2.config(state = tk.NORMAL)
        entry4_2.delete('1.0', 'end')
        entry4_2.insert(tk.INSERT, 0)
        entry4_2.config(state = tk.DISABLED)

        entry3_4.config(state = tk.NORMAL)
        entry3_4.delete('1.0', 'end')
        entry3_4.insert(tk.INSERT, 0)
        entry3_4.config(state = tk.DISABLED)

        entry4_4.config(state = tk.NORMAL)
        entry4_4.delete('1.0', 'end')
        entry4_4.insert(tk.INSERT, 0)
        entry4_4.config(state = tk.DISABLED)

        entry4_6.config(state = tk.NORMAL)
        entry4_6.delete('1.0', 'end')
        entry4_6.insert(tk.INSERT, 0)
        entry4_6.config(state = tk.DISABLED)

        this_week = True
        this_month = True
        mon_over = True
        time = int (datetime.datetime.now().strftime('%j'))
        weekday = int (datetime.datetime.now().strftime('%w'))
        monthday = int (datetime.datetime.now().strftime('%d'))
        # if weekday == 0:
        #     weekday = 7
        for item in cost_list.get_children():
            ltimeo = datetime.datetime.strptime(str(cost_list.item(item,
                                                'values')[0]), '%Y-%m-%d\
                                                %H:%M:%S  %a')
            ltime = int(ltimeo.strftime('%j'))
            # 本月
            if monthCal(ltimeo):
                calcu_eat = False
                cost_list.item(item, tag = 'this_month_tag')
                tcost = float(cost_list.item(item, 'values')[1])
                tcostreason = str(cost_list.item(item, 'values')[2])
                for eatType in eatTypes:
                    if tcostreason.find(eatType) != -1:
                        calcu_eat = True
                thisWeekEat(tcost, False, True, calcu_eat)
                thisWeek(tcost, False, True)
            # 上周周日至今天为止
            if time - ltime <= weekday:
                calcu_eat = False
                cost_list.item(item, tag = 'this_week_tag')
                tcost = float(cost_list.item(item, 'values')[1])
                tcostreason = str(cost_list.item(item, 'values')[2])
                for eatType in eatTypes:
                    if tcostreason.find(eatType) != -1:
                        calcu_eat = True
                thisWeekEat(tcost, True, False, calcu_eat)
                thisWeek(tcost, True, False)
    def inputCost():
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S  %a')
        # Mon Tue Wed Thu Fri Sat Sun 
        tcost = float(entry2_4.get())
        tfor = entry2_6.get()
        cost_list.insert('', 0, values = (time, tcost, tfor),
            tag = 'this_week_tag')
        remianF(tcost)
        # if tfor.find("买菜") != -1:
        #     calcu_eat = True
        # elif tfor.find("包子") != -1:
        #     calcu_eat = True
        # elif tfor.find("炸鸡") != -1:
        #     calcu_eat = True
        # else:
        #     calcu_eat = False
        calcu_eat = False
        for eatType in eatTypes:
            if tfor.find(eatType) != -1:
                calcu_eat = True
        thisWeekEat(tcost, True, True, calcu_eat)
        thisWeek(tcost, True, True)
    def inputkey(event):
        inputCost()
    def deleteCost():
        titem = cost_list.selection()[0]
        tcost = float(cost_list.item(titem, 'values')[1])
        tcost = -tcost
        remianF(tcost)
        # time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry3_6.delete('1.0','end')
        cost_list.delete(titem)
        weekCost()
    def deletekey(event):
        deleteCost()
    def selectClick(event):
        entry3_6.config(state = tk.NORMAL)
        titem = cost_list.selection()[0]
        tdate = cost_list.item(titem, 'values')[0]
        # print (tdate)
        entry3_6.delete('1.0','end')
        entry3_6.insert(tk.INSERT, tdate)
        entry3_6.config(state = tk.DISABLED)
    button2_8 = tk.Button(frame2, text = 'Add in',
                            font = ("Microsoft YaHei Mono", 8),
                            command = inputCost)
    button3_8 = tk.Button(frame3, text = 'Delete',
                            font = ("Microsoft YaHei Mono", 8),
                            command = deleteCost)

    # 组件打包
    # f1
    cost_list.pack(side = tk.LEFT)
    scrb.pack(side = tk.LEFT, fill = tk.Y)
    frame1.grid(row = 0, column = 0)
    # f2
    label2_1.grid(row = 0, column = 0)
    entry2_2.grid(row = 0, column = 1)
    label2_3.grid(row = 0, column = 2)
    entry2_4.grid(row = 0, column = 3)
    label2_5.grid(row = 0, column = 4)
    entry2_6.grid(row = 0, column = 5)
    label2_7.grid(row = 0, column = 6)
    button2_8.grid(row = 0, column = 7)
    frame2.grid(row = 1, column = 0, sticky = 'w', pady = 10)
    # f3
    label3_1.grid(row = 0, column = 0)
    entry3_2.grid(row = 0, column = 1)
    label3_3.grid(row = 0, column = 2, padx = 5)
    entry3_4.grid(row = 0, column = 3)
    label3_5.grid(row = 0, column = 4, padx = 9)
    entry3_6.grid(row = 0, column = 5)
    label3_7.grid(row = 0, column = 6)
    button3_8.grid(row = 0, column = 7)
    frame3.grid(row = 2, column = 0, sticky = 'w')
    # f4
    label4_1.grid(row = 0, column = 0)
    entry4_2.grid(row = 0, column = 1)
    label4_3.grid(row = 0, column = 2, padx = 5)
    entry4_4.grid(row = 0, column = 3)
    label4_5.grid(row = 0, column = 4, padx = 9)
    entry4_6.grid(row = 0, column = 5)
    label4_7.grid(row = 0, column = 6)
    frame4.grid(row = 3, column = 0, sticky = 'w', pady = 10)
    # f
    frame.pack(padx = 10, pady = 12)
    cost_list.bind('<ButtonRelease-1>', selectClick)
    entry2_4.bind('<Return>', inputkey)
    entry2_6.bind('<Return>', inputkey)
    cost_list.bind('<Delete>', deletekey)
    entry2_2.insert(tk.INSERT, 0)
    entry2_2.config(state = tk.DISABLED)
    entry3_6.config(state = tk.DISABLED)
    scrb.config(command = cost_list.yview)
    
    # 初始化
    # download_file(ftp, r"cost.ini", r"./cost_calculator/cost.ini")
    f = open('./cost_calculator/cost_local.ini', 'r', encoding='utf8')
    
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

            # sqlstr = ''
            # sqlid  = ''
            # connect = pymssql.connect('localhost', 'sa', '123456', 'costcal')
            # cursorDelete = connect.cursor()
            # cursorDelete.execute("DELETE FROM [dbo].[costlist]")
            # connect.commit()
            # cursorDelete.close()
            for item in cost_list.get_children():
                lines += cost_list.item(item, 'values')[0] + '\n'
                lines += cost_list.item(item, 'values')[1] + '\n'
                lines += cost_list.item(item, 'values')[2] + '\n'

                # sqlstr = "'" + cost_list.item(item, 'values')[0] + "', "
                # sqlstr = sqlstr + cost_list.item(item, 'values')[1] + ", "
                # sqlstr = sqlstr + "'" + cost_list.item(item, 'values')[2] + "'"
                # cursorInsert = connect.cursor()
                # cursorInsert.execute("INSERT INTO [dbo].[costlist]\
                #     ([date], [cost], [for])\
                #     VALUES (" + sqlstr + ")")
                # connect.commit()
                # cursorInsert.close()
            # connect.close()
            f = open('./cost_calculator/cost_local.ini', 'w', encoding='utf8')
            f.writelines(lines)
            f.close()
            # upload_file(ftp, r"cost.ini", r"./cost_calculator/cost.ini")
            # print (onlineOutput.split("\n"))
            root.destroy()

    def _focusNext(widget):
        '''Return the next widget in tab order'''
        widget = root.tk.call('tk_focusNext', widget._w)
        if not widget: return None
        if widget.string == '.!frame.!frame2.!button':
            return root.nametowidget('.!frame.!frame2.!entry')
        return root.nametowidget('.!frame.!frame2.!entry2')

    def OnTextTab(event):
        '''Move focus to next widget'''
        widget = event.widget
        next = _focusNext(widget)
        next.focus()
        return "break"

    weekCost()
    root.bind('<Tab>', OnTextTab)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    entry2_4.focus()
    root.mainloop()

if __name__ == "__main__":
    
    # ftp = ftp_connect("ftp.3i35.top", "GuardiansAA", "123456")
    # download_file(ftp, r"cost.ini", r"./cost_calculator/cost.ini")
    # upload_file(ftp, r"cost.ini", r"./cost_calculator/cost.ini")
    costCalculator()
