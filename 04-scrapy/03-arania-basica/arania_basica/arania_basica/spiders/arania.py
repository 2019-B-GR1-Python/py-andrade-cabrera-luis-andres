import scrapy


class IntroSpider(scrapy.Spider):
    """docstring fo IntroSpider."""
    name = "introduccion_spider"
    urls = ["http://books.toscrape.com/index.html"]
    flag_to_continue = True

    def start_requests(self):
        while(self.flag_to_continue):
            for url in self.urls:
                yield scrapy.Request(url=url)
                print("La url es: " + url + " con " + str(len(self.urls)))

    def parse(self, response):
        if len(self.urls) == 1:
            etiqueta_contenedora_categorias = response.css(
                'div.side_categories')
            nombre_categorias = etiqueta_contenedora_categorias.css(
                'li > ul > li > a::text').extract()
            nombre_categorias = [nombre_categoria.replace("\n                            \n                                ", "").replace(
                "\n                            \n                        ", "") for nombre_categoria in nombre_categorias]
            links_to_tags = etiqueta_contenedora_categorias.css(
                'li > ul > li > a::attr(href)').extract()
            links_to_tags = ["http://books.toscrape.com/" +
                             link for link in links_to_tags]
            #print("Extraccion categorias...")
            # print(nombre_categorias)
            #print("Extraccion links a categorias")
            # print(links_to_tags)
            self.urls.extend(links_to_tags)
            # print("\nEXISTEN:" + str(len(self.urls))
            f = open("/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/04-scrapy/03-arania-basica/arania_basica/books.csv", "w+")
            f.write("Title;Image_url;cost\n")
            f.close()
            self.flag_to_continue = True
        else:
            print("Entrando a ELSE con..." + str(len(self.urls)) + "\n")
            etiqueta_contenedora = response.css('article.product_pod')
            titulos = etiqueta_contenedora.css('h3 > a::text').extract()
            # print(titulos)
            links_to_images = etiqueta_contenedora.css(
                'div.image_container > a > img::attr(src)').extract()
            links_to_images = [link.replace(
                "../../../../", "http://books.toscrape.com/") for link in links_to_images]
            # print("\n")
            # print(links_to_images)
            prices_books = etiqueta_contenedora.css(
                'div.product_price > p.price_color::text').extract()
            # print("\n")
            # print(prices_books)
            self.delete_first_url()
            if not(len(response.css('.next>a::attr(href)').extract()) == 0):
                temp_list_url = response.url.split("/")
                temp_list_url[-1] = response.css(
                    '.next>a::attr(href)').extract_first()
                new_url_to_add = "/"
                new_url_to_add = new_url_to_add.join(temp_list_url)
                self.urls.append(new_url_to_add)
            #print("Escribiendo a CSV...")
            self.write_to_csv(titulos, links_to_images, prices_books)
            #print("Saliendo a ELSE... Existen: " + str(len(self.urls)))
            if (len(self.urls) == 4):
                self.flag_to_continue = False

    def delete_first_url(self):
        self.urls.pop(0)

    def write_to_csv(self, titulos, links_to_images, prices_books):
        f = open("/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/04-scrapy/03-arania-basica/arania_basica/books.csv", "a+")
        for(title, image_url, cost) in zip(titulos, links_to_images, prices_books):
            f.write("\"" + title + "\";\"" +
                    image_url + "\";" + cost + "\n")
        f.close()
    # category_urls =
    # def get_all_books_from_url(response):
