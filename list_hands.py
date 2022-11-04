from functools import reduce

data_list = [{'project_id': '14', 'project_name': '项目名称'}, {'project_id': '12', 'project_name': '第er47735三共长疗程'},
             {'project_id': '16', 'project_name': '阿斯利康'}, {'project_id': '12', 'project_name': '第er47735三共长疗程'}]
data_list.insert(0, [])
res = reduce(lambda x, y: x if y in x else x + [y], data_list)
print(res)

print(len(data_list))