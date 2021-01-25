import scrapy
import urllib
import requests
from scrapy import Request
from scrapy.http import FormRequest


class DmozItem(scrapy.Item):
	Event_id = scrapy.Field()
	Event_description = scrapy.Field()

class Logs(scrapy.Item):
    name = "logs"
    start_urls = [
    'https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/'
    ]
