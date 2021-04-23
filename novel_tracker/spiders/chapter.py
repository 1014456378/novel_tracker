import scrapy

from novel_tracker.items import Chapter


class ChapterSpider(scrapy.Spider):
    name = "chapter"
    allowed_domains = []
    start_urls = [
        "https://read.qidian.com/chapter/hbIfVTSpixsEGYrhBm4H8w2/UtU3j7SgUdnM5j8_3RRvhw2",
    ]

    def parse(self, response):
        with open('/tmp/body.txt', 'wb') as f:
            f.write(response.body)

        title = self.get_title(response)
        content = self.get_content(response)

        chapter = Chapter(title=title, content=content)
        return chapter

    @staticmethod
    def get_title(response):
        title = response.xpath('//h3[@class="j_chapterName"]/span/text()').extract()[0].strip()
        return title

    @staticmethod
    def get_content(response):
        content = ''
        for p in response.xpath('//div[@class="read-content j_readContent"]/p'):
            content += p.extract().strip().replace('</p>', '\n').replace('<p>', '')
        return content
