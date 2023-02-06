import scrapy

'''
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://brickset.com/sets/year-2019']
'''

'''
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.80/index.html']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first()
            }
'''

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first()
            }

# To recurse next page
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first()
        if next_page:
            # print("Next Page")
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
