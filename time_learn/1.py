import datetime
import time

res = datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=7)
print(res)

print(time.gmtime())

print(time.strftime('%Y-%m-%d %X'))

t = '2001-07-25 13:00:00'
res = time.strptime(t, '%Y-%m-%d %X')
print(res)
print(time.mktime(res))

print(time.asctime())

print(time.ctime())

print(datetime.datetime.now())

print(datetime.datetime.fromtimestamp(1111))
