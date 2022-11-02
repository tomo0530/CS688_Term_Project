# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesummaryItem(scrapy.Item):
    title = scrapy.Field()
    summary = scrapy.Field()
    starring = scrapy.Field()
    director = scrapy.Field()
    content = scrapy.Field()
