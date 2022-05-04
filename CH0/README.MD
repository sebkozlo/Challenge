---------------------------------- Challenge_01 ----------------------------------

http://www.pythonchallenge.com/pc/def/0.html

The challenge_01 is relatively simple, on the page we see a picture of a CRT moinor and on the screen we see the number 238.

Hint: try to change the URL address.

Changing 0 to 238 in URL is unfortunately not the correct solution.
The photo shows that the number 2 is lower than 38, which means 38 is the power of 2.

Solution:

2\*\*38 = 274877906944

The only thing left to do is change the number 0 to 274877906944.
The simplest method is copy / paste, but let's try to automate the process a bit using python.

1. Find URL image and download them.
2. Convert image as much as possible to read numbers with OCR.
3. Exponentiation.
4. Generate new URL adres.
