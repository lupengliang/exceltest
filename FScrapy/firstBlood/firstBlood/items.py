# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstbloodItem(scrapy.Item):
    # define the fields for your item here like:
    content = scrapy.Field()  # Field是一个万能的数据类型
