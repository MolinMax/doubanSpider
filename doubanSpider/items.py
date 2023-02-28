# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # 排名
    ranking = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 电影名
    name = scrapy.Field()
    # 评分
    rating = scrapy.Field()
    # 评价人数
    people = scrapy.Field()
    # 影评
    quote = scrapy.Field()
    # pass
