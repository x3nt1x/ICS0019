import scrapy


class WebSpider(scrapy.Spider):
    name = 'WebSpider'
    start_urls = ['https://arvutitark.ee/arvutid-ja-lisad/heliseadmed/mikrofonid']
    custom_settings = {
        'LOG_ENABLED': False,
        'FEEDS': {
            'scrapy_data.json': {
                'indent': 4,
                'format': 'json',
                'encoding': 'utf-8',
                'overwrite': True
            }
        }
    }

    def parse(self, response, **kwargs):
        for product in response.css('.catalogue-product'):
            yield {
                'title': product.css('._name::attr(title)').get(),
                'price': product.css('.price-html::text').get() + product.css('.price-html-decimal::text').get(),
                'picture': product.css('img::attr(src)').get()
            }

        next_page = response.css('.-right a::attr(href)').get()

        if next_page:
            yield response.follow(response.urljoin(next_page), self.parse)
