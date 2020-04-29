import scrapy
import csv
#news_title=[]
#news_description=[]


class mbminews(scrapy.Spider):
	name = "mbmi_news"
	start_urls = ['https://www.mathrubhumi.com/topics/Tag/Drug%20Case']
	
	def parse(self, response):
		SET_SELECTOR = 'div.row.listPg-md7-rw a::attr(href)'
		for href in response.css(SET_SELECTOR):
			url=response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_url)
	def parse_url(self,response):
		sel1='div.clearfix h1::text'
		sel2='div.col-md-12.col-sm-12.col-xs-12 p::text'
		#news={}
		#news['Data']=[]
		news_title=response.css(sel1).extract()
		news_description=response.css(sel2).extract()
		#for i in range(len(news_title)):
			#news['Data'].append({news_title[i][0] : news_description[i][0]})
		#print(news_description[4])
		with open('news.csv', 'a+', newline='\n') as file:
			writer = csv.writer(file)
			writer.writerow(news_title)
			writer.writerow(news_description)
		#if(cnt==0):
		#	with open('news.csv', 'w', newline='\n') as file:
		#		writer = csv.writer(file)
		#		writer.writerow(news_title)
		#		writer.writerow(news_description)
		#		cnt=1
		#		file.close()
		#with open('data.txt', 'w') as outfile:
			#json.dump(news, outfile)
			

