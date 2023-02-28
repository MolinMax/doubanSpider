# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from collections import Iterable


class DoubanspiderPipeline:
    def __init__(self):
        print("====star====")
        self.sql = pymysql.connect(host='localhost', user='root', password='password', db='py', port=3306, charset='utf8')
        self.cursor = self.sql.cursor()

    def process_item(self, item, spider):
        tplt = "{0:10}\t{1:{6}^60}\t{2:{6}^10}\t{3:{6}^10}\t{4:{6}^10}\t{5:{6}^10}"
        print(tplt.format("排名", "图片", "电影名", "评分", "人数", "描述", chr(12288)))
        data = "insert into doubanspider(ranking,pic,name,rating,people,quote) value (%s,%s,%s,%s,%s,%s);"
        for i in range(25):
            print(tplt.format(item["ranking"][i],
                              item["pic"][i],
                              item["name"][i],
                              item["rating"][i],
                              item["people"][i],
                              item["quote"][i], chr(12288)))
            value = (item["ranking"][i],
                     item["pic"][i],
                     item["name"][i],
                     item["rating"][i],
                     item["people"][i],
                     item["quote"][i])
            try:
                self.cursor.execute(data, value)
                print(value)
                self.sql.commit()
            except:
                self.sql.rollback()
                print("数据库连接失败！")
        return item

def close_spider(self, spider):
    self.cursor.close()
    self.sql.close()
    print("爬虫结束")
