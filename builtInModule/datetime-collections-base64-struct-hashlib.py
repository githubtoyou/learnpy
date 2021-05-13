#-*- coding = utf-8 -*-
#@Time:2021/5/1210:10
#@Author:Charlie
#@File:datetime-collections-base64-struct-hashlib.py
#@Software:PyCharm
import os, types, logging, pdb, sys, functools, unittest

from datetime import datetime
from datetime import timedelta
# now = datetime.now()
# nt = now.timestamp()
# print(now)
# # print(type(now))
# print(datetime.utcfromtimestamp(nt))
# dt = datetime(2015,4,19,12,20)
# print(dt)
# print(dt.timestamp())
# print(type(dt))
# t = 1615417290
# print(datetime.fromtimestamp(t))
# cday = datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
# print(cday)
# print(now.strftime('%a, %b %d %H:%M'))

# print(now + timedelta(hours=10))
# print(now + timedelta(days=1))
# print(now + timedelta(days=2, hours=10, minutes=2))

from datetime import  datetime, timedelta, timezone
# tz_utc_8 = timezone(timedelta(hours=8))
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8)
# print(dt)

# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))

import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    # 首先，获取用户输入的时间的datetime
    input_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    # 上面得到的datetime是没有时区的，因此设置用户输入的对应时区
    # 那么此时需要利用正则获取用户输入的时区
    time_zone_num = re.match(r'UTC([+|-][\d]{1,2}):00', tz_str).group(1)
    time_zone = timezone(timedelta(hours=int(time_zone_num)))  # 创建时区UTC-？？

    # 将上面得到的datetime强制设置为UTC-？？
    input_dt_tz = input_dt.replace(tzinfo=time_zone)

    return input_dt_tz.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')