import scrapy


class AraniaCrawlFybeca(scrapy.Spider):
    name = "arania_fybeca"
    start_urls = ["https://manganelo.com/"]

    def parse(self, response):
        print("Parsing...")
        genres = response.xpath(
            '//div[@class = "panel-category"]/p[@class = "pn-category-row"]/a/@title').getall()
        print(genres)
        for genre in genres:
            print(genre.replace(" Manga", ""))
            saveGenre(genre.replace(" Manga", ""))
