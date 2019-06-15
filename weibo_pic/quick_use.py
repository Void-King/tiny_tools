import os
import sys
name = input('输入微博昵称：\n')
cmda = 'cmd /k cd ' + sys.path[0] + '& python weibo_download.py -u ' + name
r = os.system(cmda)
print (r.read())
r.close()