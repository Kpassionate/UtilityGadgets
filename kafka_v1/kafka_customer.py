# -*- coding: utf-8 -*-
import config
from kafka import KafkaConsumer

consumer = KafkaConsumer(config.TOPIC,
                         bootstrap_servers=config.SERVER,
                         group_id='test2',
                         auto_offset_reset='earliest')
print(consumer.bootstrap_connected())  # 是否成功连接
print(consumer.topics())  # topic set

for msg in consumer:
    print(eval(str(msg.value, 'utf-8')))
