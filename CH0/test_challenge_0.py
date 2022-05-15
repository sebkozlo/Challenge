import unittest
import os
from challenge_0 import ImageNumberReader
from challenge_0 import ExponentiationLinkGenerator

read_number_from_image = ImageNumberReader
exponentiation_link_generator = ExponentiationLinkGenerator


class TestChallenge(unittest.TestCase):

    
    def test_image_download_positive(self):
       
       folder_path = os.listdir("./CH0")
       self.assertIn('temp_image.jpg', folder_path, msg= f"File 'temp_image.jpg' isin't in path")

    def test_image_download_negative(self):
       
       folder_path = os.listdir("./CH0")
       self.assertNotIn('temp_image.jpg', folder_path, msg= f"File 'temp_image.jpg' is in path")

    def  test_reading_number_from_url_positive(self):
        number_expected = 38
        self.assertEqual(read_number_from_image.read_number(self), number_expected, msg= f"It's should be {number_expected}.")

    def test_reading_number_from_url_negative(self):
        number_expected = 38
        self.assertNotEqual(read_number_from_image.read_number(self), number_expected, msg= f"It's should be {number_expected}.")



    # def test_number_exponentiation(self):
    #     correct_number = 274877906944
    #     self.assertEqual(exponentiation_link_generator.number_exponentiation, correct_number, msg= f"It's should be 274877906944.")

    # def test_create_new_url(self):
    #     correct_url = 'http://www.pythonchallenge.com/pc/def/274877906944.html'
    #     self.assertEqual(read_class.create_new_url(),correct_url, msg= f"It's should be {correct_url}.")
        

if __name__ == '__main__':
    unittest.main()