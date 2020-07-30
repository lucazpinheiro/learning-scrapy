import scrapy

class PostsSpider(scrapy.Spider):
    name = 'books'

    start_urls = [
        'http://books.toscrape.com/'
    ]

    def parse(self, response):
        """get entire html document
        from url"""

        for book in response.css('div ol.row'):
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get()
            }


        # page = response.url.split('/')[-2]
        # filename = f'{page}.html'

        # with open(filename, 'wb') as f:
        #     f.write(response.body)

