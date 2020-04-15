import tkinter as tk
import sys
import os
import windnd

def setVirtualDrive():
    root = tk.Tk()
    root.title("Set Virtual Drive")
    root.resizable(0, 0)

    label1 = tk.Label(root, text = "Paste or Drag the address into:")
    entry1 = tk.Entry(root, width = 50)
    frame1 = tk.Frame(root)
    label2 = tk.Label(frame1, text = "Drive:")
    entry2 = tk.Entry(frame1, width = 3)

    def dragFunc(ls):
        entry1.delete(0, tk.END)
        for i in ls:
            entry1.insert("end",i.decode("gbk")+'\n')
    def cmdCall():
        # print (entry1.get())
        os.popen("start cmd /c \"subst " + entry2.get()
                    + ": " + entry1.get() +"&&subst\"")
    def cmdCalloff():
        # print (entry1.get())
        os.popen("start cmd /c \"subst " + entry2.get()\
                    + ": /D\"")

    windnd.hook_dropfiles(entry1.winfo_id(), dragFunc)
    
    label1.pack(padx = 10, pady = 6, anchor = 'w')
    entry1.pack(padx = 13, pady = 5, anchor = 'w')
    frame1.pack(padx = 10, pady = 5)

    entry1.insert(0, "D:\Code\Work\EAP")
    entry2.insert(0, "N")
    
    label2.grid(row = 0, column = 0, padx = 0, pady = 6)
    entry2.grid(row = 0, column = 1, padx = 10, pady = 6)

    button1 = tk.Button(frame1, width = 12, text = "Load",\
                            command = cmdCall)
    button2 = tk.Button(frame1, width = 12, text = "Unload",\
                            command = cmdCalloff)

    button1.grid(row = 0, column = 2, padx = 40, pady = 6)
    button2.grid(row = 0, column = 3, padx = 7, pady = 6)

    root.mainloop()

if __name__ == "__main__":
    setVirtualDrive()
    # cmdCall("pass")
