import scrapy


class Novel(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    chapter_list = scrapy.Field()


class Chapter(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
