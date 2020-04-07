import sys
import os
import tkinter as tk
import time
# test
def mainloop():
    root = tk.Tk()
    root.title('Wifi')

    frame = tk.Frame(root)
    frame.pack()
    label1 = tk.Label(frame, text = "wifi-name:")
    label1.grid(row = 0, column = 0, padx = 20, pady = 10)
    label2 = tk.Label(frame, text = "wifi-pass:")
    label2.grid(row = 1, column = 0, padx = 20, pady = 10)
    entry1 = tk.Entry(frame)
    entry1.grid(row = 0, column = 1, padx = 20, pady = 10)
    entry2 = tk.Entry(frame)
    entry2.grid(row = 1, column = 1, padx = 20, pady = 10)
    def createwifi():
        namew = entry1.get()
        passw = entry2.get()
        print ('netsh wlan set hostednetwork mode=allow ssid='+\
                namew + ' key=' + passw)
        # r = os.popen('netsh wlan set hostednetwork mode=allow ssid='+\
        #     namew + ' key=' + passw)
        # r.close()
        time.sleep(1)
        # r = os.popen('netsh wlan start hostednetwork')
        # r.close()
        print ('netsh wlan start hostednetwork')
    def closewifi():
        # r = os.popen('netsh wlan stop hostednetwork')
        # r.close()
        # time.sleep(1)
        # r = os.popen('netsh wlan set hostednetwork mode=disallow')
        # r.close()
        print ('close')
    button1 = tk.Button(frame, text = 'Close', command = closewifi)
    button1.grid(row = 2, column = 0, padx = 20, pady = 10)
    button2 = tk.Button(frame, text = 'Create', command = createwifi)
    button2.grid(row = 2, column = 1, padx = 20, pady = 10)
    root.mainloop()


if __name__ == "__main__":
    mainloop()