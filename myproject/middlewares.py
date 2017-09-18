# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random,requests,pymongo
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class MyprojectSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This + is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyproxiesMiddleware(object):
    def __init__(self):
        self.client = pymongo.MongoClient()
        self.db = self.client.proxies
        self.proxys = self.db.ip

    def fin(self):
        ipset=[]
        a=self.proxys.find()
        for i in a:
            ipset.append(i['ip'])
        count=1

        try:
            p = random.choice(ipset)
            ip = {'http': '%s' % p}
            r = requests.get(url='https://www.baidu.com/?tn=90294326_hao_pg', proxies=ip, timeout=1)
            return ('http://%s'%p)
        except:
            while count < 3:
                try:
                    p = random.choice(ipset)
                    ip = {'http': '%s' % p}
                    r = requests.get(url='https://www.baidu.com/?tn=90294326_hao_pg', proxies=ip, timeout=1)
                    return ('http://%s' % p)
                except:
                    count+=1



    def process_request(self,request,spider):
        ip=self.fin()
        request.meta['proxy']= ip




class UserAgentMiddleware(object):
    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers.setdefault('User-Agent', random.choice(self.user_agent))