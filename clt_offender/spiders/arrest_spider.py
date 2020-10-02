import scrapy
import json


class ArrestSpider(scrapy.Spider):
    name = "arrests"

    def start_requests(self):
        urls = [
            'https://mecksheriffweb.mecklenburgcountync.gov/Arrest/_Details?arrestNum=1804535',
            'https://mecksheriffweb.mecklenburgcountync.gov/Arrest/_Charges?arrestNum=1804535'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        print(jsonresponse)
        filename = f'arrests.txt'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')