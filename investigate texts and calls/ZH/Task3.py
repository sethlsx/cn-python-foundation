"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。
"""

# 1、定义函数beiboda()，以特定区号和记录列表做输入，返回被特定区号拨打所有电话号码列表
def beiboda(quhao, jilu_list):
	haomaliebiao = []
	for jilu in jilu_list:
		if jilu[0][:len(quhao)] == quhao:
			haomaliebiao.append(jilu[1])
		else:
			pass
	return haomaliebiao

# 2、定义函数qianzhui(),以号码列表为输入，返回非重复的区号及移动前缀列表
def qianzhui(haoma_list):
	qianzhuiliebiao = []
	for haoma in haoma_list:
		if haoma[0] == '(':
			l = 0
			for i in range(len(haoma)):
				if haoma[i] == ')':
					l = i + 1
					break
				else:
					pass
			if haoma[:l] not in qianzhuiliebiao:
				qianzhuiliebiao.append(haoma[:l])
		elif haoma[0] == '7' or haoma[0] == '8' or haoma[0] == '9':
			if haoma[:4] not in qianzhuiliebiao:
				qianzhuiliebiao.append(haoma[:4])
		else:
			pass
	return qianzhuiliebiao

#3、 调用函数，输出结果

num_list = beiboda('(080)', calls)
pre_list = sorted(qianzhui(num_list))
print('The numbers called by people in Bangalore have codes:\n')
for i in range(len(pre_list)):
	print(pre_list[i] + '\n')

"""
第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

# 1、 定义函数jishu()，以号码列表及特定区号为输入，统计含有特定区号的号码的数量，返回该数量

def jishu(quhao, haoma_list):
	count = 0
	for haoma in haoma_list:
		if haoma[:len(quhao)] == quhao:
			count += 1
	return count

# 2、 调用函数，输出结果

banjialuo = jishu('(080)', num_list)
baifenbi = round((banjialuo/len(num_list) * 100), 2)

print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(baifenbi))





