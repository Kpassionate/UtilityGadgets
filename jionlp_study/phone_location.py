import jionlp as jio

# 获取手机归属地、运营商
text = '联系电话：13288568202. (021)32830431'
num_list = jio.extract_phone_number(text)
print(num_list)
# num_list = ['18401069816']
res = [jio.phone_location(item) for item in num_list]
print(res)
