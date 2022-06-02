import cv2
import pytesseract
from urllib import request
import os
from bs4 import BeautifulSoup
import requests


url_website = 'http://www.pythonchallenge.com/pc/def/0.html'
r = requests.get(url_website)
soup = BeautifulSoup(r.content, 'html.parser')
img_link = soup.find('img').attrs

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url_image = 'http://www.pythonchallenge.com/pc/def/calc.jpg'
path = 'temp_image.jpg' 


class ImageNumberReader:   
    
    def __init__(self, url_image, path):

        assert url_image.endswith((".jpg",".png")), f"Wrong url path ({url_image}), accepts only .jpg or .png file"
        assert path.endswith((".jpg",".png")), f"Wrong file name ({path}), specify extension, accepts: .jpg .png file."

        self.url_image = url_image
        self.path = path

    def download_image_from_url_to_path(self):
        """ Download image from url to path """
        request.urlretrieve(url_image, path)

    def image_convert_to_read_number(self): 
        """ Convert image to be readable by tersseract """
        self.__image_croping()
        self.__image_thresholding()

             
    def __image_croping(self, start_x= 150, end_x= 260, start_y= 265,  end_y= 440 ):
        """ Cropp image to specific dimension. 
        start_x  --- starting pixel on x axis
        end_x --- last pixel on x axis
        start_y  --- starting pixel on x axis
        end_y --- last pixel on x axis
        """
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


    def __image_thresholding(self, max_pixel_value = 255, block_size = 111, constant = 30):
        """ Change image to 8-bit grayscale and add threshold. 
        max_pixel_value --- it specifies the maximum value which is assigned to pixel values exceeding the threshold.
        block_size --- it is the size of a pixel neighbourhood that is used to calculate a threshold value.
        constant --- a constant value that is subtracted from the mean or weighted sum of the neighbourhood pixels.
            
        """
        assert max_pixel_value <= 255, f'Max pixel value must be between 0-255'
        assert max_pixel_value >= 0, f'Max pixel value must be between 0-255'
        assert block_size <= 255, f'Pixel block must be odd number between 0-255'
        assert block_size % 2 > 0 , f'Pixel block must be odd number'

        self.max_pixel_value = max_pixel_value
        self.block_size = block_size

        image_to_threshold = cv2.imread(path, 0) # 0 parameter change image to grayscale image
        image_to_threshold = cv2.adaptiveThreshold(image_to_threshold, max_pixel_value, 
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant) 
        cv2.imwrite(path, image_to_threshold) 

    def read_number_from_image(self):  
        """ Reads text from image and returns to variable """

        global read_number
        read_number = pytesseract.image_to_string(path)
        read_number = int(read_number)
        print(read_number)


class ExponentiationLinkGenerator():
    """ Exponentiation operation and creat new url adres """
    def __init__(self, base_number, pow_number):
        self.base_number = base_number
        self.pow_number = pow_number
        
    def number_exponentiation(self):
        """ Number exponentiation """
        global exponentiation_result
        exponentiation_result = pow(self.pow_number, self.base_number)
        print(exponentiation_result) 
        

    def create_new_url(self, url_to_convert, exponentiation_result):
        """ Create new url adres """
        self.url_to_convert = url_to_convert
        self.exponentiation_result = exponentiation_result
        global new_url
        new_url = self.url_to_convert.replace('0', str(exponentiation_result))
        new_url = str(new_url)
        print(new_url)
        return new_url
        
        
    def open_web_browser_new_url(self, new_url):
        """ Open chrome browser with generated link and delete path file (temp_image) """
        self.new_url = new_url
        os.system('start chrome ' + self.new_url)
        os.remove(path)

def main():
    """ Main function"""
    image_number_reader = ImageNumberReader(url_image, path)
    image_number_reader.download_image_from_url_to_path()
    image_number_reader.image_convert_to_read_number()
    image_number_reader.read_number_from_image()
    exponentiation_link_generator = ExponentiationLinkGenerator(read_number, 2)
    exponentiation_link_generator.number_exponentiation()
    exponentiation_link_generator.create_new_url(url_website, exponentiation_result)
    exponentiation_link_generator.open_web_browser_new_url(new_url)

if __name__ == "__main__":
    main()


