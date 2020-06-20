# pip install pymysql
# import pymysql

# if __name__ == "__main__":
    # url = 'bestcdn-mianban-sdkjsd.hkcc.site'
    # user = 'rypoxmla'
    # password = 'ivTRBkRY'
    # dbname = 'rypoxmla'
    # connect = pymysql.connect(
    #     host=url,
    #     port=3313,
    #     user='rypoxmla',
    #     passwd='ivTRBkRY',
    #     db='rypoxmla',
    #     charset='utf8'
    # )
    # if connect:
    #     print ('success')

    # # cursorInsert = connect.cursor()
    # # cursorInsert.execute("INSERT INTO [dbo].[costlist]\
    # #     ([date], [cost], [for])\
    # #     VALUES ('test1', -12, 'test')")
    # # connect.commit()
    # # cursorInsert.close()
    
    # cursorSelect = connect.cursor()
    # cursorSelect.execute("SELECT * FROM costlist")
    # row = cursorSelect.fetchone()
    # while row:
    #     print (row)
    #     row = cursorSelect.fetchone()
    # cursorSelect.close()
    # connect.close()

import tkinter as tk


class SampleApp(tk.Tk):

    

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        

        e1 = tk.Entry(self)
        e2 = tk.Entry(self)
        e3 = tk.Entry(self)

        e1.insert(0,"1")
        e2.insert(0,"2")
        e3.insert(0,"3")

        e1.pack()
        e2.pack()
        e3.pack()

        # reverse the stacking order to show how
        # it affects tab order
        new_order = (e3, e2)
        for widget in new_order:
            widget.lift()
        self.bind('<Tab>', self.OnTextTab)

    def _focusNext(self, widget):
        '''Return the next widget in tab order'''
        widget = self.tk.call('tk_focusNext', widget._w)
        if not widget: return None
        print (widget.string)
        if widget.string == '.!entry3':
            return self.nametowidget('.!entry2')
        return self.nametowidget(widget.string)

    def OnTextTab(self, event):
        '''Move focus to next widget'''
        widget = event.widget
        next = self._focusNext(widget)
        next.focus()
        return "break"

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()