import json
import re
import scrapy

from novel_tracker.items import Novel


class ChapterListSpider(scrapy.Spider):
    name = "chapter_list"
    allowed_domains = []
    start_urls = [
        "https://book.qidian.com/info/1019664125#Catalog",
    ]

    def parse(self, response):
        with open('/tmp/body.txt', 'wb') as f:
            f.write(response.body)

        novel_info = self.get_novel_info(response)
        name = novel_info.get('name')
        author = novel_info.get('author')

        chapter_list = self.get_chapter_list(response)

        novel = Novel(name=name, author=author, chapter_list=json.dumps(chapter_list))
        return novel

    @staticmethod
    def get_novel_info(response):
        name = response.xpath('//div[@class="book-info "]/h1/em/text()').extract()[0].strip()
        author = response.xpath('//div[@class="book-info "]/h1/span/a[@class="writer"]/text()').extract()[0].strip()
        return {
            'name':  name,
            'author': author,
        }

    @staticmethod
    def get_chapter_list(response):
        return [{
            'title': chapter.xpath('a/text()').extract()[0].strip(),
            'url': re.match('//(?P<url>.*)', chapter.xpath('a/@href').extract()[0].strip()).group('url').strip(),
        } for chapter in response.xpath('//ul[@class="cf"]/li')]


