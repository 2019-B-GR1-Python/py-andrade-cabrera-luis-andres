import scrapy
import sqlite3
import csv
import re


class AraniaCrawlGeneros(scrapy.Spider):
    name = "Get_genres"
    start_urls = ["https://manganelo.com/"]

    def parse(self, response):
        print("Parsing...")
        genres = response.xpath(
            '//div[@class = "panel-category"]/p[@class = "pn-category-row"]/a/@title').getall()
        print(genres)
        for genre in genres:
            print(genre.replace(" Manga", ""))
            saveGenre(genre.replace(" Manga", ""))


class AraniaCrawlAnime(scrapy.Spider):
    name = "Get_titles_links"  # heredado(override)
    start_url = "https://manganelo.com/genre-all"
    allowed_domains = ["manganelo.com"]
    number_pages = [i for i in range(2, 200)]
    urls = [start_url]
    for page in number_pages:
        urls.append(start_url + "/" + str(page))

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        titles = response.xpath(
            "//div[@class = \"content-genres-item\"]/div[@class = \"genres-item-info\"]/h3/a[@class = \"genres-item-name text-nowrap a-h\"]/text()").getall()
        links_to_titles = response.xpath(
            "//div[@class = \"content-genres-item\"]/div[@class = \"genres-item-info\"]/h3/a/@href").getall()
        last_chapters = response.xpath(
            "//div[@class = \"content-genres-item\"]/div[@class = \"genres-item-info\"]/a[@class = \"genres-item-chap text-nowrap a-h\"]/text()").getall()
        views = response.xpath(
            "//div[@class = \"content-genres-item\"]/div[@class = \"genres-item-info\"]/p[@class = \"genres-item-view-time text-nowrap\"]/span[@class = \"genres-item-view\"]/text()").getall()
        last_update_dates = response.xpath(
            "//div[@class = \"content-genres-item\"]/div[@class = \"genres-item-info\"]/p[@class = \"genres-item-view-time text-nowrap\"]/span[@class = \"genres-item-time\"]/text()").getall()
        authors = response.xpath(
            "//div[@class = \"content-genres-item\"]/div[@class = \"genres-item-info\"]/p[@class = \"genres-item-view-time text-nowrap\"]/span[@class = \"genres-item-author\"]/text()").getall()
        self.write_to_csv(titles, links_to_titles, last_chapters,
                          views, last_update_dates, authors)

    def write_to_csv(self, titulos, links_titulos, ultimos_caps, vistas, fecha_actualizacion, autores):
        f = open("/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/proyectos/2do_bimestre/mangas.csv", "a+")
        # f.write(
        #    "\"Titulo\";\"Link\";\"Vistas\";\"Autor(es)\";\"Ultima actualizacion\";\"Ultimo Capitulo\"\n")
        for(title, links_to_title, last_chapter, views, last_update_dates, authors) in zip(titulos, links_titulos, ultimos_caps, vistas, fecha_actualizacion, autores):
            # print("\"" + title + "\";\"" + links_to_title
            # + "\";\"" + views + "\";\"" + authors + "\";\"" +
            # last_update_dates + "\";" + last_chapter + "\n")
            # f.write("\"" + title + "\";\"" + links_to_title + "\";\"" + views.replace(",","") + "\";\"" +
            #        self.clean_author_name(authors) + "\";\"" + last_update_dates + "\";" + self.get_chapters(last_chapter) + "\n")
            f.write(title + ";" + links_to_title + ";" + views.replace(",","") + ";" +
                    self.clean_author_name(authors) + ";" + last_update_dates + ";" + self.get_chapters(last_chapter) + "\n")
        f.close()

    def get_chapters(self, last_chapter):
        before_two_points = last_chapter.split(":", 1)
        after_chapter_word = before_two_points[0].split("Chapter ",1)
        return after_chapter_word[1]

    def clean_author_name(self, author):
        pattern = "^[\x00-\x7F]+$"
        result = re.match(pattern, author)
        if result:
            return author.strip()
        else:
            return "unknown"




class AraniaCrawlGetMoreDataAnime(scrapy.Spider):
    name = "Get_full_data"
    start_urls = []
    dict_mangas = []

    def start_requests(self):
        self.get_urls_from_csv()
        print(len(self.start_urls))
        for url in self.start_urls:
            yield scrapy.Request(url)

    def parse(self, response):
        title = response.xpath('//div[@class = "story-info-right"]/h1/text()').getall()
        authors = response.xpath(
            '//div[@class = "story-info-right"]/table[@class = "variations-tableInfo"]/tbody/tr/td[@class = "table-value"]/a[@rel = "nofollow"]/text()').getall()
        status = response.xpath(
            '//div[@class = "story-info-right"]/table[@class = "variations-tableInfo"]/tbody/tr/td[@class = "table-value"]/text()').getall()
        genres = response.xpath(
            '//div[@class = "story-info-right"]/table[@class = "variations-tableInfo"]/tbody/tr/td[@class = "table-value"]/a/text()').getall()
        for author in authors:
            genres.remove(author)
        rating = response.xpath(
            '//div[@class = "story-info-right"]/div[@class = "story-info-right-extent"]/p/em/em/em[2]/em/em[1]/text()').getall()
        votes = response.xpath(
            '//div[@class = "story-info-right"]/div[@class = "story-info-right-extent"]/p/em/em/em[@property = "v:votes"]/text()').getall()
        # print(authors, status, genres, rating, votes)
        dict_manga = self.get_incomplete_dict_manga(title)
        temporal_manga = Manga(dict_manga["titulo"], self.get_status(status), dict_manga["ultimaActualizacion"], int(dict_manga["vistas"]), rating[0], float(dict_manga["last_chapter"]), int(votes[0]))
        saveManga(temporal_manga, authors, genres)

    def get_urls_from_csv(self):
        with open("/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/proyectos/2do_bimestre/mangas.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                self.start_urls.append(row["link"])
                self.dict_mangas.append(row)

    def get_status(self, status):
        if ("Ongoing" in status):
            return "Ongoing"
        else:
            return "Completed"

    def get_incomplete_dict_manga(self, title):
        for manga in self.dict_mangas:
            if(manga["titulo"] == title[0]):
                return manga



def getdb():
    db = sqlite3.connect(
        '/home/andres/Dropbox/6to&7moSemestre/IDW/py-andrade-cabrera-luis-andres/proyectos/2do_bimestre/mangas.db')
    return db


def getCur():
    cur = getdb().cursor()
    return cur


def exec(command):
    # Use all the SQL you like
    cur = getdb().cursor()
    cur.execute(command)
    getdb().commit()
    # db.close()
    return cur


def saveGenre(genre):
    query = "INSERT INTO Genero (nombre) values (\"" + genre + "\");"
    cur = getdb().cursor()
    cur.execute(query)
    cur.connection.commit()
    return cur


def check_autor_existence(author):
    query = "select count(nombre) from Autor where nombre=\'" + \
        author + "\';"
    cur = getdb().cursor()
    cur.execute(query)
    for row in cur.fetchall():
        result = row[0]
    cur.connection.close()
    return result


def saveAuthor(authors):
    for author in authors:
        if (check_autor_existence(author) == 0):
            query = "INSERT INTO Autor (nombre) values (\"" + author + "\");"
            cur = getdb().cursor()
            cur.execute(query)
            cur.connection.commit()
            return cur
        else:
            return


def getMangaID(title):
    query = "select idManga from Manga where titulo = \"" + title + "\";"
    cur = getdb().cursor()
    cur.execute(query)

    idManga = ''
    for row in cur.fetchall():
        idManga = row[0]
    cur.connection.close()
    return str(idManga)


def getGenreID(genre):
    query = "select idGenero from Genero where nombre = \"" + genre + "\";"
    cur = getdb().cursor()
    cur.execute(query)

    idGenero = ''
    for row in cur.fetchall():
        idGenero = row[0]
    cur.connection.close()
    return str(idGenero)


def getAuthorID(author):
    query = "select idAutor from Autor where nombre = \"" + author + "\";"
    cur = getdb().cursor()
    cur.execute(query)

    idAutor = ''
    for row in cur.fetchall():
        idAutor = row[0]
    cur.connection.close()
    return str(idAutor)


def saveAuthorManga(authorID, mangaID):
    cur = getdb().cursor()
    cur.execute(
        "INSERT INTO AutorManga (idAutor, idManga) values (?, ?);", (authorID, mangaID))
    cur.connection.commit()
    return cur


def saveGenreManga(genreID, mangaID):
    cur = getdb().cursor()
    cur.execute(
        "INSERT INTO GeneroManga (idGenero, idManga) values (?, ?);", (genreID, mangaID))
    cur.connection.commit()
    return cur


def saveManga(manga, authors, genres):
    cur = getdb().cursor()
    cur.execute("INSERT INTO Manga(titulo, estado, ultimaActualizacion, vistas, rating, capitulos, votos) values (?,?,?,?,?,?,?)",
                (manga.titulo, manga.estado, manga.ultimaActualizacion, manga.vistas, manga.rating, manga.capitulos, manga.votos))
    cur.connection.commit()
    saveAuthor(authors)
    idManga = getMangaID(manga.titulo)
    for author in authors:
        idAuthor = getAuthorID(author)
        saveAuthorManga(idAuthor, idManga)
    for genre in genres:
        idGenre = getGenreID(genre)
        saveGenreManga(idGenre, idManga)


class Manga:
    def __init__(self, titulo, estado, ultimaActualizacion, vistas, rating, capitulos, votos):
        self.titulo = titulo
        self.estado = estado
        self.ultimaActualizacion = ultimaActualizacion
        self.vistas = vistas
        self.rating = rating
        self.capitulos = capitulos
        self.votos = votos
