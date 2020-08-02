import scrapy

class PostsSpider(scrapy.Spider):
    name = 'posts'

    start_urls = [
        'https://dev.to/'
    ]


    # def string_formater(self, scraped_string):
    #     #remove emoji characters, this might break with non western language strings
    #     formated_string = scraped_string.encode('ascii', 'ignore').decode('ascii')
    #     return formated_string.strip()

    def parse(self, response):
        for post in response.css('div.crayons-story'):
            yield {
                'post title': post.css('div.crayons-story__indention h2 a::text').get(),
                'post author': post.css('div.crayons-story__indention h2 a::text').get(),
                'post tags': [tag.get() for tag in post.css('div.crayons-story__tags a::text')]
            }

