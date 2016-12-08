# --*-- coding:utf8 --*--
"""
JSONファイル生成コマンド
scrapy runspider crawling_handler.py -o stations.json

クローラーコマンド
scrapy crawl 名前
"""
import scrapy
from scrapy.spiders import BaseSpider
from scrapy_djangoitem import DjangoItem
from app.models.crawling.crawling_model import CrawlingModel


class CrawlingComItem(DjangoItem):
    """
    クローラーItem設定
    """
    django_model = CrawlingModel



class CrawlingSpider(BaseSpider):
    """
    Spider設定
    """

    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://tomoyane.blogo.jp/archives/1056955343.html"
    ]

    def parse(self, response):
        """
        パース設定
        :param response: SelectしたItem
        :return:         Item
        """

        title = response.xpath('//title/text()').extract()[0]
        description = "\n".join(response.xpath('//ul/li/text()').extract()).strip()
        thumbnail_url = response.css('link').xpath('@href').extract()[0]
        page_url = response.url

        return CrawlingComItem(title=title, description=description, thumbnail_url=thumbnail_url, page_url=page_url)


    def some_callback(self, response):
        """
        コールバック設定
        :param response: コールバック
        :return:         リクエスト
        """
        some_arg = 'test'
        return scrapy.Request('http://www.example.com', callback=lambda r: self.other_callback(r, some_arg))



    def other_callback(self, response, some_arg):
        """
        他コールバック設定
        :param response: None
        :param somearg:  None
        :return:         パラメータ
        """
        print "the argument passed is:", some_arg