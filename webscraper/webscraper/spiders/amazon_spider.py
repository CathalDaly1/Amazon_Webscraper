# -*- coding: utf-8 -*-
import scrapy
from ..items import WebscraperItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.co.uk/Soundcore-Microphones-Reduction-Waterproof-Earphones-Black/dp/B07SJR6HL3/ref=sr_1_3?crid=1I5YKQ2NX3104&dchild=1&keywords=anker+wireless+earphones&qid=1591010123&sprefix=anker%2Caps%2C136&sr=8-3']

    def parse(self, response):
        items = WebscraperItem()
        product_name = response.css('#productTitle::text').extract()
        product_price = response.css('#price_inside_buybox').css('::text').extract()
        stock_status = response.css('.a-color-success').css('::text').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['stock_status'] = stock_status

        strippedName = [elem.strip().split(';') for elem in product_name]
        strippedPrice = [elem.strip().split(';') for elem in product_price]
        strippedStock = [elem.strip().split(';') for elem in stock_status]

        print("****Product name: " + str(strippedName) + "****")
        print("****Product price: " + str(strippedPrice) + "****")
        print("****Product stock status: " + str(strippedStock) + "****")

        list2 = [strippedName, strippedPrice, strippedStock]
        print(list2[0])

        # yield items

