import datetime

res = datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=7)
print(res)
