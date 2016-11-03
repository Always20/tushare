#coding:utf-8
import urllib2
import re


def get_page(url):
	if url is None:
		return
	response = urllib2.urlopen(url)
	if response.getcode() != 200:
		return
	
	return response.read()


#/api/resources/startups/74959/media/303572@!picb
def get_img(page):
	reg = r'src="(\/api\/resources\/startups\/74959\/media\/3035[0-9]{2}@!picb)"
	imgre = re.compile(reg)
	imglist = re.findall(imgre, page)
	
	x=0
	for imgurl in imglist:
		urllib2.urlretrieve(imgurl, 'E:\Work_Dir\Python\Pics_Crawl\%s.jpg' % x)
		x+=1

page = get_page('http://www.evervc.com/startups/74959')
print get_img(page)
	
	

	
	

#http://www.evervc.com/startups/74959