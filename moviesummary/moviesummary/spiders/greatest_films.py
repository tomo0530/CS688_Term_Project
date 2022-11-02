import scrapy
import logging


class GreatestFilmsSpider(scrapy.Spider):
    name = 'greatest_films'
    allowed_domains = ['www.filmsite.org']
    start_urls = ['https://www.filmsite.org/momentsindx1.html']

    def clean_text(self, text):
        if text:
            return " ".join(text.split())
        return text

    def parse(self, response):
        logging.info(response.url)

        titles = response.xpath('//a/b/font[contains(@size, 4)]/text()')
        summaries = response.xpath(
            '//img[contains(@src, "summary")]/following::text()[1]')
        starrings = response.xpath(
            '//b[contains(text(), "Starring")]/following::text()[1]')
        directors = response.xpath(
            '//b[contains(text(), "Director")]/following::text()[1]')
        contents = response.xpath(
            '//img[contains(@src, "summary")]/following::text()[3]')

        for title, summary, starring, director, content in zip(titles,
                                                               summaries,
                                                               starrings,
                                                               directors,
                                                               contents):
            yield {
                'title': self.clean_text(title.get()),
                'summary': self.clean_text(summary.get()),
                'starring': self.clean_text(starring.get()),
                'director': self.clean_text(director.get()),
                'content': self.clean_text(content.get())
            }

        next_page = response.xpath(
            '//a[contains(@href, "momentsindx") and not(contains(@href, "momentsindx200"))][.//img[contains(@src, "nextpage.gif")]]/@href').get()
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
