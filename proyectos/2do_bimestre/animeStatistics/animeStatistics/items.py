# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimestatisticsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    views = scrapy.Field()
    last_chapter_published_date = scrapy.Field()
    authors = scrapy.Field()
    chapters = scrapy.Field()
    rating = scrapy.Field()
    status = scrapy.Field()
    link = scrapy.Field()
    genres = scrapy.Field()
    pass
