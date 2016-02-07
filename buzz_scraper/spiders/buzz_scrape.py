# -*- coding: utf-8 -*-
import scrapy
from buzz_scraper.items import BuzzScraperItem
from HTMLParser import HTMLParser

#HTML tag stripper to deal with item titles with embedded html like: "This is a <i>list</i> item"
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

class BuzzScraperSpider(scrapy.Spider):
    name = "buzz_scraper"
    allowed_domains = ["buzzfeed.com"]
    start_urls = []

    url_list = open('./buzz_posts.txt')
    for url in url_list:
        start_urls.append('http://' + url.rstrip())
    url_list.close()

    def parse(self, response):
        item = BuzzScraperItem()
        item['post_title'] = response.css("#post-title::text").extract_first()
        post_items = response.css(".buzz_superlist_item h2.subbuzz_name").extract()

        #Strip html from post items
        sanitized_post_items = []
        for post_item in post_items:
            no_html_tags = strip_tags(post_item)

            #make sure post_item is item
            if any(char.isdigit() for char in no_html_tags):
                sanitized_post_items.append(strip_tags(post_item))

        item['post_items'] =  sanitized_post_items

        if len(item['post_items']) > 0:
            yield item

