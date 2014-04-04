from urllib2 import urlopen
from urlparse import urlparse, urljoin

class Crawler:
    def __init__(self):
        self.seed_url = ""
        self.to_crawl_queue = []
        self.crawled = []

    def crawl(self):
        while self.to_crawl_queue:
            link = self.to_crawl_queue.pop(0)

            if link not in self.crawled:
                self.crawl_link(link)
                self.crawled.append(link)

        print "Crawl complete"

    def crawl_link(self, link):
        pass
        

    def open(self, link):
        try:
            url_object = urlopen(link)
        except urllib2.URLError:
            print "Invalid seed url"
            return
        
        redirected_url = url_object.geturl()
        redirected_url_object = urlopen(redirected_url)
        
        return redirected_url_object

    def get_page(self, url):
        try:
            page = url.read()
        except:
            page = ""
        return page

    def convert_to_absolute(self, seed_url, link):
        parsed_link = urlparse(link)
        if not parsed_link.scheme:
            return urljoin(seed_url, link)
        return link
        
