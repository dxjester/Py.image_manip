# -*- coding: utf-8 -*-
"""
FILENAME: image_manip.py
PROJECT: image_manip
DATE CREATED: 27-Nov-19
DATE UPDATED: 27-Nov-19
VERSION: 1.0
"""


#----------------------------------- START -----------------------------------#
#--------------------------- PHASE 1: Program Setup --------------------------#
#-----------------------------------------------------------------------------#

# 1.0: Module import ---------------------------------------------------------#
# import the required modules
import pandas as pd
import numpy as np
import PIL

import requests
import time
import datetime

import matplotlib.pyplot as plt

# from collections import Counter
# from string import punctuation

# 1.1: Class Declaration -----------------------------------------------------#
class image_file: 
    
    def __init__ (self, filename, file_ext):
        self.filename = filename
        self.extension = file_ext
        self.image_data = PIL.Image.open(filename)
        self.image_array = np.array(self.image_data)
    
    def display_image(self):
        self.image_data.show()
    
    def convert_array_to_image(self, array, save_filename):
        convert_image = PIL.Image.fromarray(array, 'RGB')
        filename = save_filename + '.jpg'
        path = '/image_files/' + filename
        convert_image.save(path)
        
    def return_array(self):
        return self.image_array
    
    
# 1.2: Function Declaration --------------------------------------------------#
def convert_array_to_image(array, save_filename):
    convert_image = PIL.Image.fromarray(array, 'RGB')
    filename = save_filename + '.jpg'
    path = '/image_files/' + filename
    convert_image.save(filename)
    
def flatten(image_array, flat_category):
    if (flat_category == 'F') or (flat_category == 'f'):
        image_flat = image_array.flatten('F')
    else:
        image_flat = image_array.flatten()
    return image_flat
    


#----------------------------------- START -----------------------------------#
#---------------- PHASE 2: Individual Image Processing -----------------------#
#-----------------------------------------------------------------------------#

# 2.0: Import laptop.jpg file and retrieve administrative information --------#          
laptop = image_file('laptop.jpg', 'jpg') # import 'laptop.jpg' file in local directory
laptop.display_image() # display the image

laptop_origin = laptop.return_array() # store array in local variable
laptop_origin.shape

# flatten array by row
laptop_flat_row  = laptop_origin.flatten()
laptop_flat_row

# flatten array by column
laptop_flat_col  = laptop_origin.flatten('F')
laptop_flat_col

laptop_x_length, laptop_y_length,laptop_z_length = laptop_origin.shape # shape is (3024, 4032, 3)
len(laptop_origin)



# 2.1: Image manipulation ----------------------------------------------------#
# copy the original laptop origin
laptop_copy = laptop_origin.copy()
convert_array_to_image(laptop_copy, 'laptop_copy_image')


# flip image upside down
laptop_trans = laptop_copy[::-1]
convert_array_to_image(laptop_trans, 'laptop_trans_image')


# invert the colors
laptop_invert = 255 - laptop_copy
plt.figure(figsize = (10,8))
plt.imshow(laptop_invert, cmap = plt.get_cmap('gray'))
convert_array_to_image(laptop_invert, 'laptop_invert_image')

# convert to grayscale
laptop_grayscale = np.dot(laptop_copy[...,:3], [0.299, 0.587, 0.144])
plt.figure(figsize = (10,8))
plt.imshow(laptop_grayscale, cmap = plt.get_cmap('gray'))

convert_array_to_image(laptop_grayscale, 'laptop_grayscale_image')
