# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    cod = scrapy.Field()  # not unique
    img = scrapy.Field()
    name = scrapy.Field()
    form = scrapy.Field()  # can be None
    type1 = scrapy.Field()
    type2 = scrapy.Field()  # can be None
    total = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    spatk = scrapy.Field()
    spdef = scrapy.Field()
    speed = scrapy.Field()
