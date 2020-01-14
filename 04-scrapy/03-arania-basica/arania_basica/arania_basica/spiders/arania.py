import scrapy
class IntroSpider(scrapy.Spider):
    """docstring fo IntroSpider."""
    name = "introduccion_spider"
    urls = [
        "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        # Ejercicio 0 titulos
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        print(titulos)
        # Primer ejercicio imagenes del libro
        links_to_images = etiqueta_contenedora.css('div.image_container > a > img::attr(src)').extract()
        links_to_images = [link.replace("../../../../", "http://books.toscrape.com/") for link in links_to_images]
        print("\n")
        print(links_to_images)
        # Segundo Ejercicio precios
        prices_books = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        print("\n")
        print(prices_books)
        # Tercer Ejercicio precios
        #category_urls = 
    #def get_all_books_from_url(response):
