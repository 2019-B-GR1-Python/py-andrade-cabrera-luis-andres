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
```
    response.css('.row > div > div:nth-child(2) > .text::text').extract()
```
### scrapy shell `xpath`
```
    response.xpath('/html/head/title').extract()
```
```
    response.xpath('//title').extract()
```
```
    response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
```
```
    response.xpath('/html/body/div/div[2]/div[2]/h2/text()').extract()
```
```
    response.xpath("//div[@class='quote']").extract_first()
```
```
    response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
```
```
    response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
```
```
    response.xpath("//div[@class='quote']/span/a/@href").extract_first()
```

## Scrapy startproject `nombre_proyecto`
```
    scrapy startproject arania_basica
```
