import scrapy
from bs4 import BeautifulSoup
import re
from movieScrapy.items import  HelloItem



class Hao6vCrawler(scrapy.Spider):
    name = 'hao6v'
    start_urls = ['http://www.hao6v.com']

    def parse(self, response):
        res = BeautifulSoup(response.body)
        for recommend in res.select('.pic a'):
            yield scrapy.Request(recommend['href'], self.parse_detail)

    def parse_detail(self, response):

        pattern = r'[\u4e00-\u9fa5|\s\S]*.*◎简[\s]*介[\n|\r|\s]*([\u4e00-\u9fa5|\s\S]*.*)'
        res = BeautifulSoup(response.body)
        content_wrapper = res.select('#endText')[0]
        eles = content_wrapper.find_all("p", string="◎简　　介")
        title = res.select('.col6 .box h1')[0].text

        if (len(eles) > 0):
            content = eles[0].findNext().text
        else:
            # res.select('#endText')[0].findAll('p',text=re.compile(pattern='◎简　　介'))[0].parent 加上p 是找不到的，最好不要加上p标签
            ele = content_wrapper.findAll(text=re.compile(pattern='◎简　　介'))[0].parent
            content = re.match(pattern=pattern, string=ele.text).group(1)

        item = HelloItem()
        item['title'] = title
        item['content'] = content.lstrip().replace('\r\n','')
        return item
