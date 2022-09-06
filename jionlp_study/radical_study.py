import jionlp as jio

text = '我是谁'
res = jio.char_radical(text)
for i, j in zip(text, res):
    print(i, j)
