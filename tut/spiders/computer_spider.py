import scrapy
from scrapy.loader import ItemLoader
from tut.items import ComputerItem


class ComputerSpider(scrapy.Spider):
    name = "computer"
    start_urls = [
        "https://www.komputronik.pl/search-filter/5801/komputery-do-gier?a%5B112669%5D%5B%5D=90541&filter=1&showBuyActiveOnly=0&p=1"
    ]

    def parse(self, response):
        for link in response.css("li.product-entry2 a.blank-link::attr(href)"):
            yield response.follow(link.get(), callback=self.parse_product)

        next_link = response.xpath("//i[@class='icon icon-caret2-right']/../@href")
        if next_link:
            yield response.follow(next_link.get(), callback=self.parse)

    def parse_product(self, response):
        computer_loader = ItemLoader(item=ComputerItem(), selector=response)

        computer_loader.add_css("name", "h1")
        computer_loader.add_css("price", "span.proper")
        computer_loader.add_xpath(
            "graphics", "//tr[th[contains(text(), 'Karta graficzna')]]/td"
        )

        yield computer_loader.load_item()
