# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class IntegrityPipeline:
    """Every item yielded pass thru this integrity checker.
    If one of the following attributes is missing the item is dropped.
    """
    def process_item(self, item, spider):
        if item['cod'] and item['name'] and item['type1'] \
           and item['total'] and item['hp'] and item['attack'] \
           and item['defense'] and item['spatk'] and item['spdef'] \
           and item['speed']:
            return item
        else:
            raise DropItem("Item failled on integrity pipeline %s" %
                           item)
