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

