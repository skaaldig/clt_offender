# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CltOffenderItem(scrapy.Item):
    arrest_number = scrapy.Field()
    dob = scrapy.Field()
    race = scrapy.Field()
    sex = scrapy.Field()
    weight = scrapy.Field()
    height_feet = scrapy.Field()
    height_inches = scrapy.Field()
    address = scrapy.Field()
    alias = scrapy.Field()
    name = scrapy.Field()
    arrested_by = scrapy.Field()
    arrest_date = scrapy.Field()
    arrest_time = scrapy.Field()
    court_case = scrapy.Field()
    arrest_type = scrapy.Field()
    bond = scrapy.Field()
    magistrate_initials = scrapy.Field()
    bond_type = scrapy.Field()
    arrest_process = scrapy.Field()
    arrest_description = scrapy.Field()
    mugshot_url = scrapy.Field()
    record_id = scrapy.Field()
    pass
