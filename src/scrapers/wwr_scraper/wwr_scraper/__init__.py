# Ensures the folder is treated as a Python package.
# Helps Scrapy discover spiders automatically.

__all__ = ['spiders']
from typing import Any, AsyncIterator, ClassVar, TypeVar
from scrapy.spiders import Spider
from scrapy.http import Request, Response
from scrapy.utils.trackref import object_ref
from scrapy.utils.misc import load_object
from scrapy.utils.defer import deferred_from_coro
from scrapy.utils.spider import iterate_spider_output
from scrapy.crawler import Crawler
from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.utils.log import log_scrapy_info
from scrapy.utils.python import to_unicode
from scrapy.utils.reqser import request_to_dict, request_from_dict
from scrapy.utils.response import response_to_dict, response_from_dict
from scrapy.utils.signal import send_catch_log
from scrapy.utils.defer import mustbe_deferred
from scrapy.utils.conf import build_component_list
from scrapy.utils.job import job_dir
from scrapy.extensions.closespider import CloseSpider   
from scrapy.extensions.feedexport import FeedExporter   
from scrapy.extensions.logstats import LogStats
from scrapy.extensions.memusage import MemoryUsage
from scrapy.extensions.throttle import AutoThrottle
from scrapy.extensions.telnet import TelnetConsole  
from scrapy.extensions.corestats import CoreStats           
from scrapy.extensions.spiderstate import SpiderState   
from scrapy.extensions.httpcache import HttpCacheMiddleware 
from scrapy.extensions.warnings import Warnings 
from scrapy.extensions.feedexport import FEED_EXPORTERS
from scrapy.extensions.closespider import CloseSpider
from scrapy.extensions.memusage import MemoryUsage
from scrapy.extensions.throttle import AutoThrottle
from scrapy.extensions.telnet import TelnetConsole  
from scrapy.extensions.corestats import CoreStats
from scrapy.extensions.spiderstate import SpiderState
from scrapy.extensions.httpcache import HttpCacheMiddleware