from MainCrawler import MainCrawler
from CakeCrawler import CakeCrawler
from XlsWrite    import XlsWrite
from ImageSaver  import ImageSaver

m = MainCrawler()
print "Crawling main page..."
m.crawl()

c = CakeCrawler(m.cake_list)
print "Crawling cake pages..."
c.crawl()

x = XlsWrite(c.cake_list)
print "Writing Excel sheet..."
x.populate_excel()

i = ImageSaver(c.cake_list)
print "Saving cake images..."
i.save_images()
