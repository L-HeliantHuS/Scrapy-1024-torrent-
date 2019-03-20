# -*- coding: utf-8 -*-
import scrapy
from urllib import parse



class H1024pSpider(scrapy.Spider):
    name = 'h1024p'
    allowed_domains = ['1024xp1.pw', 'downsx.rocks', 'downsx.com']
    start_urls = ['http://xh2.1024xp1.pw/pw/thread.php?fid=7&page=1']

    def parse(self, response):
        next_page_urls = response.xpath("//tr[@class='tr3 t_one']")
        for next_url in next_page_urls:
            get_url = next_url.xpath(".//td[2]/h3/a/@href").extract_first()
            if (get_url is not None) and (get_url[0] == "h"):
                url = parse.urljoin("http://xh2.1024xp1.pw/pw/", get_url)
                yield scrapy.Request(
                    url=url,
                    callback=self.get_next_page_html,
                )
            else:
                pass
        num = response.url.split("=")[-1:][0]

        url = "http://xh2.1024xp1.pw/pw/thread.php?fid=7&page={}".format(int(num) + 1)
        yield scrapy.Request(
            url=url,
            callback=self.parse
        )


    def get_next_page_html(self, response):
        torrent_page_url = response.xpath("//a[@href=text()]/@href").extract_first()

        item = {}
        item['title'] = response.xpath("//title/text()").extract_first()

        if torrent_page_url is not None:
            yield scrapy.Request(
                url=torrent_page_url,
                callback=self.get_torrent_url,
                meta={"item": item}
            )
        else:
            pass


    def get_torrent_url(self, response):
        item = response.meta['item']
        torrent = response.xpath("//a[text()='磁力連結']/@href").extract_first()
        item['torrent'] = torrent
        yield item