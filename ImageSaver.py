import urllib2
import os
import requests

class ImageSaver:
    def __init__(self, cake_list):
        self.cake_list = cake_list
        self.path = "./images/"
        

    def save_images(self):
        os.mkdir('images')
        os.chdir('images')
        for cake in self.cake_list:
            cake_name = cake.name
            img_src = cake.img_src
            self.download(cake_name, img_src)

    def download(self, cake_name, img_src):
        f = open(cake_name + '.jpg','wb')
        f.write(requests.get(img_src).content)
        f.close()
        
        
