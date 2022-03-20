# Change Log
Arquivo para documentação das mudanças realizadas ao longo do projeto. O formato desse arquivo é baseado no [Keep a Changelog](http://keepachangelog.com/)
e o presente projeto adota o [Semantic Versioning](http://semver.org/).

## [0.6.0] - 2021-11-17
### [COT-297](https://ecoanalytics.atlassian.net/browse/COT-397)
### Adicionado
- Sobrescrito a função `image_downloaded` do objeto `ImagesPipeline` para garantir a persistência de apenas imagens que ainda não estão salvas no storage.

## [0.5.1] - 2021-11-01
### [COT-294](https://ecoanalytics.atlassian.net/browse/COT-294)
#### Adicionado
- Adicionado o atributo `sku` ao objeto `ArtwalkAdidasItem`.

## [0.5.0] - 2021-10-30
### [COT-294](https://ecoanalytics.atlassian.net/browse/COT-294)
#### Adicionado
- Adicionado as spiders [`ArtWalkAdidasIvyParkSpider`, `ArtWalkFemaleNikeAF1Spider`, `ArtWalkMaleNikeAF1Spider`, `ArtWalkFemaleNikeAirMaxSpider`, `ArtWalkMaleNikeAirMaxSpider`, `ArtWalkFemaleNikeJordanSpider`, `ArtWalkMaleNikeJordanSpider`, `ArtWalkFemaleNikeLebronSpider`, `ArtWalkMaleNikeLebronSpider`, `ArtWalkKidsNikeLebronSpider`, `ArtWalkFemaleNikeSpider`, `ArtWalkMaleNikeSpider`, `ArtWalkKidsNikeSpider`]
#### Alterado
- Alterado lógica de funcionamento do monitor `ItemCountMonitor`.
#### Removido
- Retirado a persistência de imagens no tamanho 800*600.

## [0.4.1] - 2021-10-11
### [COT-236](https://ecoanalytics.atlassian.net/browse/COT-236)
#### Alterado
- Alterado a atribuição da feature `reference_first_image` na coleta.

## [0.4.0] - 2021-10-09
### [COT-202](https://ecoanalytics.atlassian.net/browse/COT-202)
#### Adicionado
- Adicionado a feature `reference_first_image` ao objeto `ArtwalkAdidasItem`. 
#### Alterado
- Alterado a configuração `IMAGES_THUMBS` para salvar imagens no padrão 400x400.

## [0.3.1] - 2021-10-09
### [COT-197](https://ecoanalytics.atlassian.net/browse/COT-149)
#### Alterado
- Alterado o parâmetro `SPIDERMON_MIN_ITEMS` para 300 da `ArtWalkAMaleAdidasOriginalsSpider`.

## [0.3.0] - 2021-10-04
### [COT-149](https://ecoanalytics.atlassian.net/browse/COT-149)
#### Adicionado
- Adicionado monitoramento por [spidermon](https://github.com/scrapinghub/spidermon).
- Adicionado monitoramento por [Sentry](https://sentry.io).

## [0.2.0] - 2021-09-23
### [COT-114](https://ecoanalytics.atlassian.net/browse/COT-114)
#### Adicionado
- Adicionado a classe `ArtWalkImagePipeline` para realizar coleta das imagens dos produtos.
- Adicionado a dependência `Pillow==8.3.2`.
- Adicionado os campos `image_urls` e `image_uris` ao objeto `ArtwalkAdidasItem`.
#### Removido
- Removido a dependência `scrapy-fieldstats`.


