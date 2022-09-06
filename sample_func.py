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

samp_list = [1, 1, 2, 0]

print(any(samp_list))
print(all(samp_list))


def do_something_with(data):
    if data ** 2 > 2:
        return data


result = [do_something_with(item) for item in samp_list if do_something_with(item)]
print(result)
result = list(filter(bool, [do_something_with(item) for item in samp_list]))
print(result, '<<<<<<<<<<>>>>>>>>>>')

old_list = [1, 3, 2, 0]
doubled_list = list(map(lambda x: x * 2, old_list))
print(doubled_list)

summation = reduce(lambda x, y: x + y, old_list)
print(summation)
print(sum(old_list))

true_list = list(filter(bool, old_list))
print(true_list)

new_dict = dict(zip(old_list, old_list))
print(new_dict)

results = [(i, j)
           for i in range(10)
           for j in range(i)]
print(results)

a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
results = []
current_max = 0
for i in a:
    current_max = max(i, current_max)
    results.append(current_max)
print(results)


def max_generator(numbers):
    current_max = 0
    for i in numbers:
        current_max = max(i, current_max)
        yield current_max


results = list(max_generator(a))
print(results)

from itertools import accumulate

a = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
results = list(accumulate(a, max))
print(results)

# 另外，如果要迭代组合序列，则需要使用product()， permutations()， combinations()。
