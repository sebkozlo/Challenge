import cv2
import pytesseract
from urllib import request

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url_website = 'http://www.pythonchallenge.com/pc/def/0.html'
url_image = 'http://www.pythonchallenge.com/pc/def/calc.jpg'
path = './temp_image.jpg'


class ReadNumberFromImage:
    

    def image_download(self):
        """Download image from url and save it in path""" 

        request.urlretrieve(url_image, path)
        image = cv2.imread(path)
        cv2.imshow('Image to read', image)
        
    def image_convert(self):
        """Converts image to readable text"""
        #-- Image crop
        image = cv2.imread(path) 
        image_crop = image[150:265, 280:440]
        cv2.imwrite(path, image_crop)
        cv2.imshow('Image crop', image_crop)

        #-- Image grayscale
        image_crop = cv2.imread(path)
        image_grayscale = cv2.cvtColor(image_crop, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Image grayscale', image_grayscale)

        #-- Image treshold
        image_treshold = cv2.adaptiveThreshold(image_grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 111, 30)
        cv2.imwrite(path, image_treshold) 
        cv2.imshow('Image treshold', image_treshold)

        #-- Uncomment below line to see conversion results
        #cv2.waitKey(0)
        cv2.destroyAllWindows()

    def image_read_number(self):
        """Reads text (numbers) from converted image and putt it in variable"""

        number_read = pytesseract.image_to_string(path)
        return int(number_read)


    def number_exponentiation(self):
        """Exponentiation number from image"""

        base_number = 2
        power_number = ReadNumberFromImage().image_read_number()
        exponentiation_result = base_number ** power_number
        return exponentiation_result
        

    def create_new_url(self):
        """Change url using replace method"""
        
        url_to_convert = url_website
        number = ReadNumberFromImage().number_exponentiation()
        new_url = url_to_convert.replace('0', str(number))
        return new_url

read_class = ReadNumberFromImage()
read_class.image_download()
read_class.image_convert()
read_class.image_read_number()
print(read_class.image_read_number())
read_class.number_exponentiation()
print(read_class.number_exponentiation())
read_class.create_new_url()
print(read_class.create_new_url())