from functools import reduce, partial

a = {1: 'A', 3: 'C', 2: 'B'}

b = sorted(a.items(), key=lambda kv: kv[0])
print(b)

c = list(filter(lambda kv: kv[0] < 3, a.items()))
print(c)

d = map(lambda kv: (str(kv[0]), kv[1]), a.items())
print(dict(d))

e = reduce(lambda x, y: x + y, a.items())
print(e)

f = [[{'1': 'A', '2': 'B'}], [{'3': 'A', '4': 'B'}]]
# 用于拆分
g = reduce(lambda x, y: x + y, f)
print(g)

h = [1, 'a', 2]

i = all(isinstance(i, int) for i in h)
print(i)
j = any(isinstance(i, int) for i in h)
print(j)


def _fun(_a, _b):
    return _a + _b


fun1 = partial(_fun, _a=1)
print(fun1(_b=2))
