import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def clean_string(value):
    return value.strip()


def clean_price(value):
    decoded = value.encode("ascii", "ignore")
    encoded = decoded.decode()
    return encoded[:-1]


class ComputerItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_string),
        output_processor=TakeFirst(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_string, clean_price),
        output_processor=TakeFirst(),
    )
    graphics = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_string),
        output_processor=TakeFirst(),
    )
