from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
import re
import json

class MySpider(object):
	"""docstring for MySpider"""
	def __init__(self, url, headers):
		self._req = request.Request(url, headers=headers)

	def contentParser(self, content):
		pass

	def getUrlData(self):
		req = self._req
		with request.urlopen(req) as qb_page:
			resp = qb_page.read()
			print('Status:', qb_page.status, qb_page.reason)
			for k, v in qb_page.getheaders():
				print('%s: %s' % (k, v))
			content = resp.decode('utf-8')
			return content

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
headers = { 'User-Agent' : user_agent }
res = {}
'''for i in range(1,35):
	url = 'https://www.qiushibaike.com/8hr/page/'+str(i)+'/?s=4985640'
	qb_spider = MySpider(url,headers)
	content = qb_spider.getUrlData()

	re_author = re.compile(r'<h2>(.*?)</h2>',re.S)
	re_content = re.compile(r'<div class="content">\n+<span>(.*?)</span>\n+</div>',re.S)
	authors = re.findall(re_author, content)
	duanzis = re.findall(re_content, content)
	
	with open('qb.json', 'w', encoding='utf-8') as f:
		for i in range(len(authors)):
			res[authors[i]] = duanzis[i]
		json.dump(res, f, ensure_ascii=False)
'''
with open('qb.json', 'r', encoding='utf-8') as f1:
	with open('qb.md', 'a', encoding='utf-8') as f2:
		content = json.load(f1)
		for k in content:
			f2.write('#' + k + '\n')
			f2.write(content[k] + '\n')
		