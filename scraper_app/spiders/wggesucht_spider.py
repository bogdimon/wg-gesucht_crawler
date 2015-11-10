from scrapy.http.request import Request
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

import re

from scraper_app.items import WGGesuchtEntry




class WGGesuchtSpider(Spider):
    """Spider for wg-gesucht.de, Berlin"""
    name = "wggesucht"
    allowed_domains = ["wg-gesucht.de"]
    start_urls = ["http://www.wg-gesucht.de/wohnungen-in-Berlin.8.2.0.0.html"]
    # start_urls = ["http://www.wg-gesucht.de/wohnungen-in-Berlin.8.2.0.%s.html"%x for x in range(0,1)]


    entries_list_xpath = '//tr[contains(@id,"ad--")]'
    item_fields = {
        # 'title': './/span[@itemscope]/meta[@itemprop="name"]/@content',
        'rooms': './/td[2]/a/span/text()',
        'entry_date': './/td[3]/a/span/text()',
        'price': './/td[4]/a/span/b/text()',
        'size': './/td[5]/a/span/text()',
        'district': './/td[6]/a/span/text()',
        'start_date': './/td[7]/a/span/text()',
        'end_date': './/td[8]/a/span/text()',
        'link': './/@adid'
    }

    # def start_requests(self):
    #     for i in xrange(1, 2):
    #         url = 'http://www.wg-gesucht.de/wohnungen-in-Berlin.8.2.0.' + str(i) + '.html'
    #         yield Request(url=url, callback=self.parse_items)


    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        # Testing contracts:
        # @url http://www.livingsocial.com/cities/15-san-francisco
        # @returns items 1
        # @scrapes title link

        """
        selector = HtmlXPathSelector(response)



        # iterate over deals
        for entry in selector.xpath(self.entries_list_xpath):
            loader = XPathItemLoader(WGGesuchtEntry(), selector=entry)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()         

        
        cur_index = response.meta.get('cur_index', 1)
        new_url = re.sub('\d+.html',str(cur_index)+'.html',response.url)

        print("\n"+ str(response.url)+"\n"+new_url+"\n")

        if cur_index < 59:
            yield Request(new_url, callback=self.parse, meta={'cur_index': cur_index+1})