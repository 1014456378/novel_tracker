import pymongo
from novel_tracker.settings import DATABASE_CONFIG


class ChapterPipeline(object):
    def __init__(self):
        self.mongodb_connect = pymongo.MongoClient(host=DATABASE_CONFIG['mongodb']['host'], port=DATABASE_CONFIG['mongodb']['port'])
        self.db = self.mongodb_connect[DATABASE_CONFIG['mongodb']['db']]

    def process_item(self, item, spider):
        if spider.name == 'chapter':
            return self._process_item(item, spider)
        return item

    def _process_item(self, item, spider):
        self.insert(item)
        return item

    def insert(self, item):
        self.db['chapter'].insert(dict(item))
