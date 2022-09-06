import jionlp as jio

text = '邮箱：2022@126.com, 手机号：16612569096, 身份证：52010320171109002X，(网站)：www.baidu.com，ip:127.0.0.1' \
       'qq: 282010166,微信：no_bug_always'
# 提取邮箱
res = jio.extract_email(text)
print(res)

# 提取身份证号
res = jio.extract_id_card(text)
print(res)

# 提取手机号
res = jio.extract_phone_number(text)
print(res)

# 提取ip
res = jio.extract_ip_address(text)
print(res)

# 提取QQ
res = jio.extract_qq(text)
print(res)

# 提取微信号
res = jio.extract_wechat_id(text)
print(res)

# 提取url
res = jio.extract_url(text)
print(res)

# 提取括号（）中的
res = jio.extract_parentheses(text)
print(res)