from Crawler import Crawler
from bs4 import BeautifulSoup
class MainCrawler(Crawler):
    def __init__(self):
        self.seed_url = "http://www.wishpicker.com/gifts-for/cakes"
        self.to_crawl_queue = [self.seed_url]
        self.crawled = []
        self.cake_list = []
        
    def crawl_link(self, link):
        link_url = self.open(link)
        link_page = self.get_page(link_url)
        soup = BeautifulSoup(link_page)

        for url in soup.find_all('link', {'rel' : 'next'}):
            fetched_link = url.get('href')
            if fetched_link:
                fetched_link = self.convert_to_absolute(link_url.geturl(), fetched_link)
                self.to_crawl_queue.append(fetched_link)
        
        for url in soup.find_all("a", "disable-click"):
            fetched_link = url.get("href")
            if fetched_link:
                fetched_link = self.convert_to_absolute(link_url.geturl(), fetched_link)
                self.cake_list.append(fetched_link)

        self.crawled.append(link)
        
            
