# Scrapy

## Scrapy instalación

    $ pip install scrapy

## Comandos generales

Da `las características` para poder hacer Web Scraping o Web Crawling de ese computador

    $ scrapy bench

Visualizar las `configuraciones extra`

    $ scrapy settings

Visualizar la `version` de scrapy

    $ scrapy version

### scrapy view `url`

Si se ve el contenido:

    $ scrapy view https://www.pluralsight.com/authors

No se ve el contenido:

    $ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT

### scrapy shell `url`
Permite interactuar con la respuesta del Scrapy
```
    $ scrapy shell http://quotes.toscrape.com/
```
```
    response.css('title')
```
```
    response.css('title').extract()
```
```
    response.css('title::text')
```
```
    response.css('title::text').extract()
```
```
    type(response.css('.author::text'))
```
```
    response.css('.author::text')[0]
```
```
    response.css('.author::text')[0].extract()
```  
```
    response.css('.tags>.tag::text').extract()
```
