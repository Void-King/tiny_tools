import datetime

time = datetime.datetime.strptime('2020-02-21', '%Y-%m-%d')
monthday = int (datetime.datetime.strptime('2020-06-19', '%Y-%m-%d').strftime('%d'))
s1 = ['2020-05-20','2020-05-19','2020-06-19']
def monthCal(time):
    time_str = datetime.datetime.now().strftime('%Y-%m-%d')
    time_now = int(datetime.datetime.now().strftime('%j'))
    monthday = int(datetime.datetime.now().strftime('%d'))
    time = int(time.strftime('%j'))
    print (time_now - time)
    if monthday > 20:
        if time_now - time < monthday - 20:
            return True
        else:
            return False
    else:
        print (time_str[5:7])
        time_str_m = str(int(time_str[5:7]) - 1)
        if int(time_str[5:7]) - 1 < 10:
            time_str_m = '0' + time_str_m
        time_str_n = time_str[:5] + str(time_str_m) + '-21'
        print (time_str)
        print (time_str_n)
        ltime = int(datetime.datetime.strptime(time_str_n,
                    '%Y-%m-%d').strftime('%j'))
        print (time - ltime)
        if time - ltime >= 0:
            return True
        else:
            return False
print (monthCal(time))
# print (monthday)
# for i in s1:
#     ltime = datetime.datetime.strptime(i, '%Y-%m-%d')
#     ltime = int(ltime.strftime('%j'))
#     if monthday >= 20:
#         if time - ltime <= monthday - 20:
#             print (i)
#     else:
#         if time - ltime < 32:
#             if time - ltime <= monthday:
#                 print (i)
#             if int(datetime.datetime.strptime(i, '%Y-%m-%d').strftime('%d')) >= 20:
#                 print (i)

