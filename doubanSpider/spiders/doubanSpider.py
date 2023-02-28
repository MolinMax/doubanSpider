import scrapy
from doubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = "doubanSpider"
    allowed_domains = ['movie.douban.com']
    # start_urls = ["https://movie.douban.com/top250?start=125"]

    start_urls = ["https://movie.douban.com/top250?start={}".format(i) for i in range(0, 251, 25)]

    # https://movie.douban.com/top250?start=25&filter=
    # https://movie.douban.com/top250?start=50&filter=

    def parse(self, response):
        all_comments = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        item = DoubanspiderItem()
        ranking =[0]*25
        pic =[0]*25
        name =[0]*25
        rating =[0]*25
        people =[0]*25
        q =[0]*25
        for v, i in enumerate(all_comments):
            ranking[v] = i.xpath('//div[@class="pic"]/em/text()').extract()[v]
            pic[v] = i.xpath('//div[@class="pic"]/a/img/@src').extract()[v]
            name[v] = i.xpath('//div[@class="hd"]/a/span[1]/text()').extract()[v]
            rating[v] = i.xpath('//span[@class="rating_num"]/text()').extract()[v]
            people[v] = i.xpath('//div[@class="star"]/span[4]/text()').extract()[v]

            w = '//li[{}]/div/div[2]/div[2]/p/span/text()'.format(v + 1)
            quote = response.xpath(w).extract()
            if quote == []:
                quote = ' '
            q[v] = quote[0]
        item["ranking"] = ranking
        # 还可以再加影片主页
        item["pic"] = pic
        item["name"] = name
        item["rating"] = rating
        item["people"] = people
        item["quote"] = q
        yield item
