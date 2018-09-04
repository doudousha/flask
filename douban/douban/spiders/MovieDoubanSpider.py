import json
import re

import scrapy
from scrapy import Request


class MovieDoubanSpider(scrapy.Spider):
    name = "movieDouban"
    custom_settings = {'DOWNLOAD_DELAY': 2}
    # allowed_domains = ["douban.com"]
    page_start = 0
    PAGE_LIMIT = 50
    MOVIE_TAG = '豆瓣高分'
    BASE_URL = "https://movie.douban.com/j/search_subjects?type=movie&tag=%s&page_limit=%s&page_start=%s"
    start_urls = [BASE_URL % (MOVIE_TAG, PAGE_LIMIT, page_start)]

    # start_urls = ['https://movie.douban.com/subject/24773958/']

    def parse(self, response):
        print('json------------------%s', response.body.decode('utf-8'))
        infos = json.loads(response.body.decode('utf-8'))


        for movie_info in infos['subjects']:
            print('输出infos---------%s'% movie_info['url'])
            print('输出cover---------%s'%movie_info['cover'])
            movie_item = {}
            movie_item['image_urls'] = {movie_info['cover']}
            yield Request(movie_info['url'], callback=self.parse_movie, meta={'_movie_item': movie_item})

    def parse_movie(self, response):
        movie_item = response.meta['_movie_item']
        # # 获取整个信息字符串
        info = response.css('div.subject div#info').xpath('string(.)').extract_first()
        # 取得所有字段名
        fileds = [s.strip().replace(':', '') for s in response.css('div#info span.pl::text').extract()]
        print(info)
        # 取得所有字段值 "?:" 不分组捕获
        # re.sub 与 string.replace 区别 sub 支持正则表达式，replace 不支持，那么意味者"hello 123 world 456" ，而你想把123和456，都换成222，这时候replace就无能为力了！
        values = [re.sub('\s+', '', s.strip()) for s in re.split('\s*(?:%s):\s*' % '|'.join(fileds), info)[1:]]

        # zip 打包为元组(1,2),(3,4)
        # dict 将元祖转换为字典
        print('0000000000000000000000000000000')
        print(dict(zip(fileds, values)))
        yield movie_item
