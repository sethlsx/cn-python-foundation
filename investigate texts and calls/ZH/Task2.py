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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

# 1、定义一个统计时长的函数tongjishichang()，以通话记录列表为输入，返回字典类型各号码通话时长统计
def tongjishichang(jilu_list):
	shichang = {}
	for jilu in jilu_list:
		if jilu[0] in shichang:
			shichang[jilu[0]] += int(jilu[3])
		else:
			shichang[jilu[0]] = int(jilu[3])

		if jilu[1] in shichang:
			shichang[jilu[1]] += int(jilu[3])
		else:
			shichang[jilu[1]] = int(jilu[3])

	return shichang


# 2、找到通话时长最长的号码

mubiaohaoma = []
mubiaoshichang = 0
shichang = tongjishichang(calls)
for haoma in shichang:
	if shichang[haoma] > mubiaoshichang:
		mubiaohaoma = []
		mubiaohaoma.append(haoma)
		mubiaoshichang = shichang[haoma]
	elif shichang[haoma] == mubiaoshichang:
		mubiaohaoma.append(haoma)
	else:
		pass

# 考虑了2种情况，只有一个最长时长的号码和有多个最长时长的号码

if len(mubiaohaoma) == 1:
	print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(mubiaohaoma[0], mubiaoshichang))
else:
	print('There are {} numbers spent the longest time, {} seconds, on the phone during September 2016. They are as followed:\n'.format(len(mubiaohaoma), mubiaoshichang))
	for i in range(len(mubiaohaoma)):
		print(str(mubiaohaoma[i]) + '\n')

