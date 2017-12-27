# 豆瓣上最好的电影项目

# 任务1:获取每个地区、每个类型页面的url

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
import urllib.parse
import requests
import expanddouban
from bs4 import BeautifulSoup
import csv

def getMovieUrl(category, location):
	relative_url = '#/?sort=S&range=9,10&tags=电影,' + category + ',' + location
	url = urllib.parse.urljoin('https://movie.douban.com/tag/', relative_url)
	return url

# 任务2:获取电影页面html
def get_html(url):
	html = expanddouban.getHtml(url, True, 3)
	return html




# 任务3:定义电影类


class Movie(object):
	def _init_(self, name, rate, location, category, info_link, cover_link):
		self.name = name
		self.rate = rate
		self.location = location
		self.category = category
		self.info_link = info_link
		self.cover_link = cover_link




# 任务4:获得豆瓣电影的信息
"""
return a list of Movie objects with the given category and location.
"""
def getMovies(category, location):
	movies = []
	url = getMovieUrl(category, location)
	html = get_html(url)
	soup = BeautifulSoup(html, 'html.parser')
	for item in soup.find(class_ = "list-wp").find_all('a'):
		movie = Movie()
		movie.name = item.find(class_ = 'title').get_text()
		movie.rate = item.find(class_ = 'rate').get_text()
		movie.location = location
		movie.category = category
		movie.info_link = item.get('href')
		movie.cover_link = item.find('img').get('src')
		movies.append(movie)
	return movies

# 调试语句
# movies = getMovies('喜剧', '美国')


# 任务5:构造电影信息数据表

types = ['喜剧', '科幻', '动作']
regions = ['大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', '法国', '德国', '意大利', 
'西班牙', '印度', '泰国', '俄罗斯', '伊朗', '加拿大', '澳大利亚', '爱尔兰', '瑞典', '巴西', '丹麦']

with open('movies.csv', 'w') as csvfile:
	file_w = csv.writer(csvfile)
	for type_ in types:
		for region in regions:
			movies = getMovies(type_, region)
			for movie in movies:
				row = [movie.name, movie.rate, movie.location, movie.category, movie.info_link, movie.cover_link]
				file_w.writerow(row)









# 任务6:统计电影数据
with open('movies.csv') as f:
	f_csv = csv.reader(f)
	category = ''
	count = {}
	location = {}
	for row in f_csv:
		if row[3] != category:
			if location:
				count[category] = location
			category = row[3]
			location= {}
		else:
			if row[2] in location:
				location[row[2]] += 1
			else:
				location[row[2]] = 1
	count[category] = location
	
	x = open('output.txt', 'w')				#增加此行使得多次运行时output.txt文件重置
	x.close()
	
	for type_ in count:
		with open('output.txt', 'a') as output:
			print('在我选择的{}类别中，数量排名前三的地区及其分别占该类别总数的百分比为：\n'.format(type_), file = output)
			first, second, third = '', '', ''
			first_num, second_num, third_num = 0, 0, 0
			sumnum = 0
			for region in count[type_]:
				sumnum += count[type_][region]
				if count[type_][region] > first_num:
					third = second
					third_num = second_num
					second = first
					second_num = first_num
					first = region
					first_num = count[type_][region]
				elif count[type_][region] < first_num and count[type_][region] > second_num:
					third = second
					third_num = second_num
					second = region
					second_num = count[type_][region]
				elif count[type_][region] < second_num and count[type_][region] > third_num:
					third = region
					third_num = count[type_][region]
				else:
					pass
			print(first + ' %.2f%%\n'%(first_num/sumnum*100), file = output)
			print(second + ' %.2f%%\n'%(second_num/sumnum*100), file = output)
			print(third + ' %.2f%%\n'%(third_num/sumnum*100), file = output)	




