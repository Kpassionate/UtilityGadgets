import jionlp as jio

text = '张三赔偿李四人民币车费601,293.11元，工厂费一万二千三百四十五元,利息9佰日元，打印费十块钱。'
# 提取金额
moneys = jio.extract_money(text)
print(moneys)

# 提取为阿拉伯数字金额对象，带币种
standard_moneys = [jio.parse_money(i) for i in moneys]
print(standard_moneys)

# 数字转大写金额
new_moneys = [1.96, 2, 4]
new_standard_moneys = [jio.money_num2char(i) for i in new_moneys]
print(new_standard_moneys)


