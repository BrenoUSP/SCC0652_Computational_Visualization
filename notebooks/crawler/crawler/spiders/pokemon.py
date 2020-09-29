"""Crawler to gather data from pokemondb."""
import scrapy
from scrapy.crawler import CrawlerProcess
from ..items import CrawlerItem

# Example entry on pokemondb for reference:
# <tr>
#     <td class="cell-num cell-fixed" data-sort-value="3">
#         <span class="infocard-cell-img">
#             <span class="img-fixed icon-pkmn"
#                   data-src="https://img.pokemondb.net/sprites/sword-shield/icon/venusaur-mega.png"
#                   data-alt="Mega Venusaur icon">
#             </span>
#         </span>
#         <span class="infocard-cell-data">003</span></td>
#     <td class="cell-name">
#         <a class="ent-name"
#            href="/pokedex/venusaur"
#            title="View pokedex for #003 Venusaur">Venusaur</a><br>
#         <small class="text-muted">Mega Venusaur</small></td>
#     <td class="cell-icon">
#         <a class="type-icon type-grass" href="/type/grass">Grass</a><br>
#         <a class="type-icon type-poison" href="/type/poison">Poison</a></td>
#     <td class="cell-total">625</td>
#     <td class="cell-num">80</td>
#     <td class="cell-num">100</td>
#     <td class="cell-num">123</td>
#     <td class="cell-num">122</td>
#     <td class="cell-num">120</td>
#     <td class="cell-num">80</td>
# </tr>


class PokeSpider(scrapy.Spider):
    """Class based on scrapy Spider for collect the data from pokemondb."""

    # Spider's name
    name = "pokemon"
    # Spider's url to crawl
    start_urls = ['https://pokemondb.net/pokedex/all']
    # Telling spider to pass every item thru integrity pipeline
    custom_settings = {"ITEM_PIPELINES": {"crawler.pipelines.IntegrityPipeline": 100}}

    def parse(self, response):
        """Parses HTML in response and yields items."""

        # Generates a list with every entry at the table (<tr>)
        pokemons = response.xpath('//table[@id="pokedex"]/tbody/tr')

        for pokemon in pokemons:
            item = CrawlerItem()
            if pokemon.xpath('./td[1]//span[@class="img-fixed icon-pkmn"]/@data-src').extract_first() != 'https://img.pokemondb.net/s.png':
                item['img'] = pokemon.xpath('./td[1]//span[@class="img-fixed icon-pkmn"]/@data-src').extract_first()
            item['cod'] = pokemon.xpath('./td[1]//span[@class="infocard-cell-data"]/text()').extract_first()
            item['name'] = pokemon.xpath('./td[2]/a/text()').extract_first()
            item['form'] = pokemon.xpath('./td[2]/small/text()').extract_first()
            item['type1'] = pokemon.xpath('./td[3]/a[1]/text()').extract_first()
            item['type2'] = pokemon.xpath('./td[3]/a[2]/text()').extract_first()
            item['total'] = pokemon.xpath('./td[4]/text()').extract_first()
            item['hp'] = pokemon.xpath('./td[5]/text()').extract_first()
            item['attack'] = pokemon.xpath('./td[6]/text()').extract_first()
            item['defense'] = pokemon.xpath('./td[7]/text()').extract_first()
            item['spatk'] = pokemon.xpath('./td[8]/text()').extract_first()
            item['spdef'] = pokemon.xpath('./td[9]/text()').extract_first()
            item['speed'] = pokemon.xpath('./td[10]/text()').extract_first()
            yield item
