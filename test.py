import time

for i in range(1,8):
    t = [2009, 2, 17, 17, 3, 38, 1, 48, 0]
    t[2] += i
    t = tuple(t)
    t = time.mktime(t)
    print (time.strftime("%a", time.gmtime(t)))
