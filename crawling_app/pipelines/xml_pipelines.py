# --*-- coding: utf8 --*--
from scrapy import signals
from scrapy.exporters import XmlItemExporter

class XmlExportPipeline(object):
    """
    XMLエクスポートクラス
    """


    def __init__(self):
        """
        Init設定
        """
        self.files = {}


    @classmethod
    def from_crawler(cls, crawler):
        """
        クローラー
        :param crawler: signal
        :return:        pipeline
        """
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline


    def spider_opened(self, spider):
        """
        XML開設定
        :param spider: xml
        :return:       None
        """
        file = open('%s_products.xml' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()


    def spider_closed(self, spider):
        """
        XML閉設定
        :param spider: xml
        :return:       None
        """
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()


    def process_item(self, item, spider):
        """
        Item設定
        :param item:   item
        :param spider: export
        :return:       item
        """
        self.exporter.export_item(item)
        return item