import jionlp as jio

text = '邮箱：2022@126.com, 手机号：16612569096, 身份证：52010320171109002X，(网站)：www.baidu.com，ip:127.0.0.1' \
       'qq: 282010166,微信：no_bug_always`</div>'
# 移除邮箱
res = jio.remove_email(text)
print(res)

# 移除身份证号
res = jio.remove_id_card(text)
print(res)

# 移除手机号
res = jio.remove_phone_number(text)
print(res)

# 移除ip
res = jio.remove_ip_address(text)
print(res)

# 移除QQ
res = jio.remove_qq(text)
print(res)


# 移除url
res = jio.remove_url(text)
print(res)

# 移除括号（）中的
res = jio.remove_parentheses(text)
print(res)

# 移除异常字符
res = jio.remove_exception_char(text)
print(res)

# 移除html标签
res = jio.remove_html_tag(text)
print(res)