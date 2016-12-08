# -*- coding: utf-8 -*-


class CrawlingAppPipeline(object):
    """
    Pipeline設定
    """
    def process_item(self, item, spider):
        item.save()
        return item
