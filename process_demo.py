#!/usr/bin/env python
# coding=utf-8
import time
import multiprocessing


def push_message(count, params_openid_list, template_data):
    time.sleep(1)
    template_data['openid_list'] = params_openid_list
    print('888*88*******开始请求发送消息接口', count, template_data)


def push_task_day():
    res = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]] * 1
    print("本次符合推送的任务数量", len(res))
    pool = multiprocessing.Pool(2)
    appid_dict = {}
    for item in res:
        app_id = item[2]
        template_id = item[3]
        keyword1 = item[4]
        keyword2 = item[5]
        keyword3 = str(item[6])
        temp_url = item[9]
        template_data = {
            "app_id": app_id,
            "template_id": template_id,
            "data": {
                "first": {"value": '观看患教直播，参与医生互动', "color": "#173177"},
                "keyword1": {"value": keyword1, "color": "#173177"},
                "keyword2": {"value": keyword2, "color": "#173177"},
                "keyword3": {"value": keyword3, "color": "#173177"},
                "remark": {"value": "直播即将开始，请准时点击观看", "color": "#173177"}
            },
            "u_type": 0,
            "url": temp_url
        }
        openid_list = appid_dict.get(app_id, list(range(1, 4039)))
        count = 0
        length = 200
        for i in range(0, len(openid_list), length):
            count += 1
            params_openid_list = openid_list[i:i + length]
            pool.apply_async(push_message, args=(count, params_openid_list, template_data), callback=print_error)
    pool.close()
    pool.join()


def print_error(value):
    print("error: ", value)


if __name__ == '__main__':
    a = time.time()
    push_task_day()
    print(time.time() - a)

# 此脚本注意错误：当在主进程中合成template_data时 数据异常
