import scrapy,re
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from myproject.items import MyprojectItem


class QuotesSpider(scrapy.Spider):
    name = ("work")
    ChemicalNameIndex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 33, 31, 32, 33, 34, 35]
    urls = [
        ['http://www.chemicalbook.com/ProductNameList_1_{}_EN.htm'.format(i) for i in range(0, 188900, 100)],
        ['http://www.chemicalbook.com/ProductNameList_2_{}_EN.htm'.format(i) for i in range(0, 210100, 100)],
        ['http://www.chemicalbook.com/ProductNameList_3_{}_EN.htm'.format(i) for i in range(0, 195300, 100)],
        ['http://www.chemicalbook.com/ProductNameList_4_{}_EN.htm'.format(i)for i in range(0, 204400, 100)],
        ['http://www.chemicalbook.com/ProductNameList_5_{}_EN.htm'.format(i)for i in range(0, 94500, 100)],
        ['http://www.chemicalbook.com/ProductNameList_6_{}_EN.htm'.format(i) for i in range(0, 55600, 100)],
        ['http://www.chemicalbook.com/ProductNameList_7_{}_EN.htm'.format(i) for i in range(0, 13100, 100)],
        ['http://www.chemicalbook.com/ProductNameList_8_{}_EN.htm'.format(i) for i in range(0, 101600, 100)],
        ['http://www.chemicalbook.com/ProductNameList_9_{}_EN.htm'.format(i) for i in range(0, 36100, 100)],
        ['http://www.chemicalbook.com/ProductNameList_11_{}_EN.htm'.format(i) for i in range(0, 4300, 100)],
        ['http://www.chemicalbook.com/ProductNameList_10_{}_EN.htm'.format(i) for i in range(0, 1400, 100)],
        ['http://www.chemicalbook.com/ProductNameList_21_{}_EN.htm'.format(i) for i in range(0, 11300, 100)],
        ['http://www.chemicalbook.com/ProductNameList_22_{}_EN.htm'.format(i) for i in range(0, 21300, 100)],
        ['http://www.chemicalbook.com/ProductNameList_23_{}_EN.htm'.format(i) for i in range(0, 31300, 100)],
        ['http://www.chemicalbook.com/ProductNameList_24_{}_EN.htm'.format(i) for i in range(0, 34800, 100)],
        ['http://www.chemicalbook.com/ProductNameList_25_{}_EN.htm'.format(i) for i in range(0, 44700, 100)],
        ['http://www.chemicalbook.com/ProductNameList_26_{}_EN.htm'.format(i) for i in range(0, 4300, 100)],
        ['http://www.chemicalbook.com/ProductNameList_27_{}_EN.htm'.format(i) for i in range(0, 44300, 100)],
        ['http://www.chemicalbook.com/ProductNameList_28_{}_EN.htm'.format(i) for i in range(0, 51500, 100)],
        ['http://www.chemicalbook.com/ProductNameList_29_{}_EN.htm'.format(i) for i in range(0, 58700, 100)],
        ['http://www.chemicalbook.com/ProductNameList_30_{}_EN.htm'.format(i) for i in range(0, 4000, 100)],
        ['http://www.chemicalbook.com/ProductNameList_31_{}_EN.htm'.format(i) for i in range(0, 6500, 100)],
        ['http://www.chemicalbook.com/ProductNameList_32_{}_EN.htm'.format(i) for i in range(0, 3200, 100)],
        ['http://www.chemicalbook.com/ProductNameList_33_{}_EN.htm'.format(i) for i in range(0, 1000, 100)],
        ['http://www.chemicalbook.com/ProductNameList_34_{}_EN.htm'.format(i) for i in range(0, 1400, 100)],
        ['http://www.chemicalbook.com/ProductNameList_35_{}_EN.htm'.format(i) for i in range(0, 10000, 100)],
    ]
    url=[]
    for i in urls:
        for l in i:
            url.append(l)
    start_urls = url

    allowed_domains = ["chemicalbook.com"]  #设置爬虫范围


    def parse(self,response):
        name_urls=response.xpath('//*[@id="ContentPlaceHolder1_ProductClassDetail"]/tr/td[2]/a/text()').extract()
        for n in name_urls:
            item=MyprojectItem()
            item['name']=n
            yield item
