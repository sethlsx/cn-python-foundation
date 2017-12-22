"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

print(str(reader))

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."

"""
#1、 定义一个统计非重复电话号码的函数
def count_numbers(origin_list):
	#	遍历列表生成集合
	haomaji = set()
	for jilu in origin_list:
		if jilu[0] not in haomaji:	#判断第一个号码是否在集合中
			haomaji.add(jilu[0])
		if jilu[1] not in haomaji:	#判断第二个号码是否在集合中
			haomaji.add(jilu[1])
	#	返回集合元素数
	return len(haomaji)

#2、 调用函数计算短信和通话记录中一共有多少电话号码

haomashu = 0
haomashu += count_numbers(texts)
haomashu += count_numbers(calls)

#3、 输出信息

print('There are {} different telephone numbers in the records.'.format(haomashu))

