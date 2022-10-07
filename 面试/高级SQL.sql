#!/usr/bin/python
# -*- coding:utf-8 -*-

sql = "select score, dense_rank() over(order by score desc) as 'rank' from scores;"

-- 生成虚拟时间
SELECT @cdate :=date_add(@cdate,INTERVAL-1 DAY) AS date FROM (
SELECT @cdate :=date_add(CURDATE(),INTERVAL+1 DAY) FROM customer LIMIT 10) a


-- 虚拟时间结合group by 结果集
SELECT aa.cdate,bb.b_date,bb.total FROM (
SELECT @cdate :=date_format(date_add(@cdate,INTERVAL-1 DAY),"%Y-%m-%d") AS cdate FROM (
SELECT @cdate :=date_add('2020-06-01 00:00:00',INTERVAL+1 DAY) FROM customer_order) a WHERE @cdate>='2019-01-01 00:00:00') aa
JOIN (
SELECT FROM_UNIXTIME(b.add_time,"%Y-%m-%d") b_date,count(1) total FROM customer b WHERE b.add_time> unix_timestamp('1572926478') GROUP BY FROM_UNIXTIME(b.add_time,"%Y-%m-%d")) bb
ON aa.cdate=bb.b_date


-- 时间戳-格式化时间的相互转换
SELECT unix_timestamp('2022-09-28 16:55:07')  # 格式化时间转时间戳
SELECT FROM_UNIXTIME('1573733105', "%Y-%m-%d") date # 时间戳转格式化时间  1573733105 2019-11-14


-- 查看入组数据
SELECT DISTINCT time FROM risk_control_id_test.xzkj_incoming_week_data


SELECT FROM_UNIXTIME(co.arrival_time+86400*8-0,"%Y-%m-%d") 应还款时间
FROM customer_order co where co.arrival_time is not null limit 10

-- 日期前置，往前推进 ep:date_sub('2019-07-27', interval 30 day)表示往前推30天
SELECT UNIX_TIMESTAMP(DATE_SUB(NOW(),INTERVAL 5 month))
-- 往前推进5个月  DATE_SUB
SELECT DATE_SUB(NOW(),INTERVAL 5 month)
-- 往后推进5个月  DATE_ADD
SELECT DATE_ADD(NOW(),INTERVAL 5 month)

-- 正则匹配
select c.nickname from customer c where c.nickname REGEXP '^tw|^JF|^ZTX|^ZHCS|^ZH|^TIN|^INDC|^NDY'  limit 10  # twlYsIOa
select c.nickname from customer c where c.nickname REGEXP 'twlYsIOa|^JF'  limit 10

-- 转换大小写
SELECT UPPER('ADMIN');
SELECT LOWER('ADMIN');



