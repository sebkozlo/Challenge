import cv2
import pytesseract
from urllib import request
import requests
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url_website = 'http://www.pythonchallenge.com/pc/def/0.html'
url_image = 'http://www.pythonchallenge.com/pc/def/calc.jpg'
path = './CH0/temp_image.jpg' 


class ImageNumberReader:   
    
    def __init__(self, url_image, path):
        self.url_image = url_image
        self.path = path

    def read_number_from_url(self):
        self.image_download(url_image)
        self.image_convert()
        self.read_number() 
        return self.read_number
        
    def image_download(self, url_image):
        self.url_image = url_image
        request.urlretrieve(url_image, path)

    def image_convert(self):        
        self.__image_crop()
        self.__image_grayscale()
        self.__image_treshold()
    
    def __image_crop(self):
        self.image_crop = cv2.imread(path) 
        self.image_crop = self.image_crop[150:265, 280:440]
        cv2.imwrite(path, self.image_crop)
        #cv2.imshow('Image crop', image_crop)

    def __image_grayscale(self):       
        self.image_grayscale = cv2.imread(path)
        self.image_grayscale = cv2.cvtColor(self.image_crop, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(path, self.image_grayscale)
        #cv2.imshow('Image grayscale', image_grayscale)

    def __image_treshold(self):
        self.image_treshold = cv2.adaptiveThreshold(image_number_reader.image_grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 30)
        cv2.imwrite(path, self.image_treshold) 
        #cv2.imshow('Image treshold', image_treshold)
        #-- Uncomment below line to see conversion results
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

    def read_number(self):        
        self.number = pytesseract.image_to_string(path)
        return int(self.number)


class ExponentiationLinkGenerator():

    def __init__(self, number):
        self.number = number
        
    def number_exponentiation(self, number):
        self.number = number
        self.exponentiation_result = pow(2, number)
        self.exponentiation_result = int(self.exponentiation_result)
        return self.exponentiation_result
        # print(self.exponentiation_result)                

    def create_new_url(self, url_to_convert, exponentiation_result):
        self.url_to_convert = url_to_convert
        self.exponentiation_result = exponentiation_result
        self.new_url = self.url_to_convert.replace('0', str(self.exponentiation_result))
        self.new_url = str(self.new_url)
        print(self.new_url)
        
    def open_web_browser_new_url(self, url):
        self.url = url
        url = str(self.new_url)
        os.system('start chrome ' + self.new_url)


image_number_reader = ImageNumberReader(url_image, path)
image_number_reader.read_number_from_url()
exponentiation_link_generator = ExponentiationLinkGenerator(image_number_reader.number)
exponentiation_link_generator.number_exponentiation(image_number_reader.read_number())
exponentiation_link_generator.create_new_url(url_website, exponentiation_link_generator.exponentiation_result)
exponentiation_link_generator.open_web_browser_new_url(ExponentiationLinkGenerator.create_new_url)
