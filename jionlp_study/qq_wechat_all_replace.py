import jionlp as jio

text = '邮箱：2022@126.com, 手机号：16612569096, 身份证：52010320171109002X，(网站)：www.baidu.com，ip:127.0.0.1' \
       'qq: 282010166,微信：no_bug_always'
# 替换邮箱
res = jio.replace_email(text)
print(res)

# 替换身份证号
res = jio.replace_id_card(text)
print(res)

# 替换手机号
res = jio.replace_phone_number(text)
print(res)

# 替换ip
res = jio.replace_ip_address(text)
print(res)

# 替换QQ
res = jio.replace_qq(text)
print(res)

# 替换url
res = jio.replace_url(text)
print(res)
