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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

#1、 建立拨出电话列表、接收电话列表、发短信列表、接收短信列表
bochu_list = []
jieshou_list = []
faduanxin_list = []
shouduanxin_list = []

for entry in calls:
	bochu_list.append(entry[0])
	jieshou_list.append(entry[1])

for entry in texts:
	faduanxin_list.append(entry[0])
	shouduanxin_list.append(entry[1])



#2、 检查哪些电话只在拨出电话列表中，而不在其他列表中，生成推销列表

tuixiao_list = []
for num in bochu_list:
	if (num not in jieshou_list) and (num not in faduanxin_list) and (num not in shouduanxin_list) and (num not in tuixiao_list):
		tuixiao_list.append(num)

tuixiao_list = sorted(tuixiao_list)
print('These num could be telemarketers:\n')
for haoma in tuixiao_list:
	print(haoma + '\n')