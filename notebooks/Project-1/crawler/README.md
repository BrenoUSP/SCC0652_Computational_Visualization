# Scrapy based crawler

Crawler to gather data from [PokemonDB](https://pokemondb.net/pokedex/all)

## To execute

```shell
scrapy crawl pokemon -o pokemon.csv -t csv
```

> Note: ```-o``` specifies the output file. ```-t``` specifies the output file type.

## Relevant files

- [```items.py```](./crawler/items.py): Define structure data fields.
- [```pokemon.py```](./crawler/spiders/pokemon.py): Define crawler's spider and its parser.
- [```pipelines.py```](./crawler/pipelines.py): Data integrity pipeline (check up).
- [```pokemon.csv```](./pokemon.csv): Pokemons data from [PokemonDB](https://pokemondb.net/pokedex/all).
