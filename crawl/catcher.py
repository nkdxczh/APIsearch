from splinter.browser import Browser
import requests
from selenium.common.exceptions import TimeoutException
import os.path

class catcher:
    def __init__(self):
        self.browser = Browser()
        self.browser.driver.set_page_load_timeout(5)

    def set_url(self, url):
        self.url = url

    def download(self, url, name):
        if os.path.exists(name):
            return
        result = requests.get(url)
        if '</html>' in result.content:
            return
        output = open(name, 'w')
        output.write(result.content)
        output.close()

    def close(self):
        self.browser.quit()

    def catch(self):
        self.browser.visit(self.url)
        frame = self.browser.find_by_tag('frameset')[1].find_by_tag('frame')[1]
        print len(frame.find_by_tag('html'))
        tmpitems = []
        for item in items:
            href = item.find_by_tag('a')
            tmpitems.append(href[0]['href'])

        for href in tmpitems:
            try:
                self.browser.visit(href)
            except TimeoutException:
                pass
            groups = self.browser.find_by_tag('a')
            for g in groups:
                #g.text
                downloadurl = str(g['href'])
                if g.text == 'Download' and downloadurl.endswith('.csv'):
                    #print downloadurl
                    #print downloadurl
                    name = downloadurl.split('/')
                    self.download(downloadurl, './data/Safety1/'+name[-1])
