import scrapy


class ApiSpider(scrapy.Spider):
    name = "api"
    start_urls = ['https://docs.oracle.com/javase/8/docs/api/overview-summary.html']
    
    def parse(self, response):
        rows = response.css('tr')[1:]
        for r in rows:
            cols = r.css('td')
            package = cols[0].css('a::text').extract_first()
            link = cols[0].css('a::attr(href)').extract_first()
            descript = cols[1].css('div::text').extract_first()
            yield response.follow(link, callback = self.parsePackage)
        '''self.fc = open('class', 'wb')
        self.fm = open('method', 'wb')
        div = response.css('div.indexContainer')
        classes = div.css('a::text').extract()
        links = div.css('a::attr(href)').extract()
        for i in range(len(classes)):
            self.fc.write(classes[i] + ':https://docs.oracle.com/javase/8/docs/api/' + links[i] + '\n')
            #yield response.follow(links[i], callback=self.parseMethod)
        self.fc.close()
        self.fm.close()'''
        '''page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)'''

    def parsePackage(self, response):
        types = response.css('table.typeSummary')
        print response.css('h1.title::text').extract_first()
        for t in types:
            print t.css('caption span::text').extract_first()

