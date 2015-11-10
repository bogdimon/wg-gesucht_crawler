from scrapy.item import Item, Field

class WGGesuchtEntry(Item):
    """WG-Gesucht container (dictionary-like object) for scraped data"""
    rooms = Field()
    entry_date = Field()
    price = Field()
    size = Field()
    district = Field()
    start_date = Field()
    end_date = Field()
    link = Field()