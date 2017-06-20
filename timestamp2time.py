import time
a = "2017-04-17 12:00:00"

# 时间转换时间戳
# print(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
print(time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S')))
