import cv2
import pytesseract
from urllib import request
import requests
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url_website = 'http://www.pythonchallenge.com/pc/def/0.html'
url_image = 'http://www.pythonchallenge.com/pc/def/calc.jpg'
path = 'temp_image.jpg' 

class ImageNumberReader:   
    
    def __init__(self, url_image, path):

        assert url_image.endswith((".jpg",".png")), f"Wrong url path ({url_image}), accepts only .jpg or .png file"
        assert path.endswith((".jpg",".png")), f"Wrong file name ({path}), specify extension, accepts: .jpg .png file."

        self.url_image = url_image
        self.path = path

    def download_image_from_url_to_path(self):
        """ Download image from url to path"""

        request.urlretrieve(url_image, path)

    def image_convert_to_read_number(self): 
        """ Convert image to be readable by tersseract."""

        self.__image_croping(150, 260, 265, 440)
        # self.__image_grayscaling()
        self.__image_tresholding()

             
    def __image_croping(self, start_x= 150, end_x= 260, start_y= 265,  end_y= 440 ):
        """ Cropping image to specific dimension. """

        image_to_crop = cv2.imread(path)
        img_height = image_to_crop.shape[0]
        img_width = image_to_crop.shape[1]

        assert start_x >= 0, "Start pixel must be equal or greater than 0"
        assert end_x <= img_height, f"End pixel must be equal or smaller than {img_height}"
        assert start_y >= 0, "Start pixel must be equal or greater than 0"
        assert end_y <= img_width, f"End pixel must be equal or smaller than {img_width}"

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

        image_to_crop = cv2.imread(path) 
        image_to_crop = image_to_crop[start_x:end_x, start_y:end_y]
        cv2.imwrite(path, image_to_crop)


    def __image_grayscaling(self):       
        """ Changing image to grayscale. """

        image_to_grayscale = cv2.imread(path)
        image_to_grayscale = cv2.cvtColor(image_to_grayscale, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(path, image_to_grayscale)


    def __image_tresholding(self):
        """ Change image to 8-bit"""

        image_to_treshold = cv2.imread(path, 0)
        image_to_treshold = cv2.adaptiveThreshold(image_to_treshold, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 30)
        
        cv2.imwrite(path, image_to_treshold) 
        cv2.imshow('Image treshold', image_to_treshold)

        cv2.waitKey(0)
        #cv2.destroyAllWindows()

#     def read_number(self):        
#         self.number = pytesseract.image_to_string(path)
#         return int(self.number)


# class ExponentiationLinkGenerator():

#     def __init__(self, number):
#         self.number = number
        
#     def number_exponentiation(self, number):
#         self.number = number
#         self.exponentiation_result = pow(2, number)
#         self.exponentiation_result = int(self.exponentiation_result)
#         return self.exponentiation_result
#         # print(self.exponentiation_result)                

#     def create_new_url(self, url_to_convert, exponentiation_result):
#         self.url_to_convert = url_to_convert
#         self.exponentiation_result = exponentiation_result
#         self.new_url = self.url_to_convert.replace('0', str(self.exponentiation_result))
#         self.new_url = str(self.new_url)
#         print(self.new_url)
        
#     def open_web_browser_new_url(self, url):
#         self.url = url
#         url = str(self.new_url)
#         os.system('start chrome ' + self.new_url)

def main():

    image_number_reader = ImageNumberReader(url_image, path)
    image_number_reader.download_image_from_url_to_path()
    image_number_reader.image_convert_to_read_number()
    

if __name__ == "__main__":
    main()

# image_number_reader.read_number_from_url()
# exponentiation_link_generator = ExponentiationLinkGenerator(image_number_reader.number)
# exponentiation_link_generator.number_exponentiation(image_number_reader.read_number())
# exponentiation_link_generator.create_new_url(url_website, exponentiation_link_generator.exponentiation_result)
# exponentiation_link_generator.open_web_browser_new_url(ExponentiationLinkGenerator.create_new_url)
