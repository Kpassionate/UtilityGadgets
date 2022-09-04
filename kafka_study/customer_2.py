# -*- coding: utf-8 -*-
import json

import config
from kafka import KafkaConsumer

consumer = KafkaConsumer(config.TOPIC,
                         bootstrap_servers=config.SERVER,
                         group_id='test',
                         auto_offset_reset='earliest') # 相同group_id共同消费同一topic数据，不同group_id可分别全部消费同一个topic
print(consumer.bootstrap_connected())  # 是否成功连接
print(consumer.topics())  # topic set

for msg in consumer:
    print(json.loads(msg.value))
    # print(eval(str(msg.value, 'utf-8')))
