import tkinter as tk
import os
import sys



root = tk.Tk()
root.title('hosts change')
frame = tk.Frame(root)
frame.grid(row = 1, sticky = tk.W, padx = 20, pady = 10)

text = tk.Text(root, font = '微软雅黑 10')
text.grid(row = 0, sticky = tk.W, padx = 25, pady = 15)

ipt = tk.Entry(frame, width = 50)
ipt.grid(row = 0, column = 0, sticky = tk.W, padx = 5, pady = 5)




def flushf():
    f = open('C:\Windows\System32\drivers\etc\hosts', 'r')
    all_hosts = f.read() + '----------------------------------------------'
    text.delete('1.0','end')
    text.insert(tk.INSERT, all_hosts)
    f.close()
    r = os.popen('ipconfig /flushdns')
    # print (r.read())
    r.close()
def insertf():
    new_hosts = ipt.get()
    fw = open('C:\Windows\System32\drivers\etc\hosts', 'a')
    new_hosts = new_hosts + '\n'
    fw.write(new_hosts)
    fw.close()
    flushf()
def deletef():
    f = open('C:\Windows\System32\drivers\etc\hosts', 'r')
    lines = f.readlines()
    f.close()
    fw = open('C:\Windows\System32\drivers\etc\hosts', 'w')
    num = len(lines)
    # print (lines)
    for line in lines:
        if num > 1:
            fw.write(line)
            num -= 1
        else:
            break
    fw.close()
    flushf()

ibt = tk.Button(frame, text = '插入', command = insertf)
ibt.grid(row = 0, column = 1, padx = 5, pady = 5)
dbt = tk.Button(frame, text = '删除', command = deletef)
dbt.grid(row = 0, column = 2, padx = 5, pady = 5)
fbt = tk.Button(frame, text = '刷新', command = flushf)
fbt.grid(row = 0, column = 3, padx = 5, pady = 5)
flushf()
root.mainloop()