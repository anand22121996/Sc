import scrapy
from ..items import ScItem

class AmazonSpider(scrapy.Spider):
    name = 'flipkart'
    start_urls = ['https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off']

    def parse(self, response):
        item = ScItem()
        product_name = response.css('._4rR01T::text').extract()
        product_price = response.css('._1_WHN1::text').extract()
        #product_link = response.css('._2QcLo- ._3exPp9::text').extract()
        i = 0
        for product in product_name:
            
            item['product_name'] = product_name[i]
            item['product_price'] = product_price[i]
            item['product_']
       # items['product_link'] = product_link
            i+=1
            yield item
        
        for p in range(2,51):    
            next_page = 'https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page='+str(p)
            if p <= 50:
                yield response.follow(next_page, callback = self.parse)