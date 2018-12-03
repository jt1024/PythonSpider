# -*- coding: utf-8 -*-

# Scrapy settings for conan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'conan'

SPIDER_MODULES = ['conan.spiders']
NEWSPIDER_MODULE = 'conan.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'conan (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'conan.pipelines.ComicImgDownloadPipeline': 1,
}

IMAGES_STORE = 'D:/DataguruPyhton/PythonSpider/images/名侦探柯南'

COOKIES_ENABLED = False

DOWNLOAD_DELAY = 0.25    # 250 ms of delay