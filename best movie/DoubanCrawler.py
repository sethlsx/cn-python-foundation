# 豆瓣上最好的电影项目

# 任务1:获取每个地区、每个类型页面的url

"""
return a string corresponding to the URL of douban movie lists given category and location.
"""
import urllib.parse
import requests
import expanddouban

def getMovieUrl(category, location):
	relative_url = '#/?sort=S&range=9,10&tags=电影,' + category + ',' + location
	url = urllib.parse.urljoin('https://movie.douban.com/tag/', relative_url)
	return url

# 任务2:获取电影页面html
def get_html(url):
	html = expanddouban.getHtml(url, True)




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


# 任务5:构造电影信息数据表


# 任务6:统计电影数据

