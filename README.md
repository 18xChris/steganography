Using an existent library for image manipulation in python I wrote a simple steganography program.\
This program read a *.png* image in the form of pixels, so the image will be codified as a list of lists.\
The outer list will be the height of the image, and the inner list will be the width, so an image 20 * 40 will have 20 lists (heigth) and 40 lists (width) for every list of the 20.\
Every pixel is represented as an RGB tuple, so (0,0,0) will indicates black.\
This program takes in input a phrase and every letter of the phrase (codified in ASCII format) is written into the first element of the image's tuples.\
The code is commented so you can understand what I have done.\
If there are problems contact me, tnx ^^.
