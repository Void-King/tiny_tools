import datetime

time = int (datetime.datetime.strptime('2020-06-19', '%Y-%m-%d').strftime('%j'))
monthday = int (datetime.datetime.strptime('2020-06-19', '%Y-%m-%d').strftime('%d'))
s1 = ['2020-05-20','2020-05-19','2020-06-19']
print (monthday)
for i in s1:
    ltime = datetime.datetime.strptime(i, '%Y-%m-%d')
    ltime = int(ltime.strftime('%j'))
    if monthday >= 20:
        if time - ltime <= monthday - 20:
            print (i)
    else:
        if time - ltime < 32:
            if time - ltime <= monthday:
                print (i)
            if int(datetime.datetime.strptime(i, '%Y-%m-%d').strftime('%d')) >= 20:
                print (i)

