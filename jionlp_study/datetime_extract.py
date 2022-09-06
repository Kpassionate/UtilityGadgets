import time
import jionlp as jio

res = jio.parse_time('今年9月', time_base={'year': 2022})
print(res)
res = jio.parse_time('零三年元宵节晚上8点半', time_base=time.time())
print(res)
res = jio.parse_time('一万个小时')
print(res)
res = jio.parse_time('100天之后', time.time())
print(res)
res = jio.parse_time('每周五下午4点', time.time())
print(res)



