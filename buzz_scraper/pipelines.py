# -*- coding: utf-8 -*-

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem("missing {0}!".format(data))

        self.collection.insert(dict(item))
        return item
