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

# 1.1: Module import ---------------------------------------------------------#
# import the required modules
import pandas as pd
import numpy as np
import PIL

import requests
import time
import datetime

import matplotlib.pyplot as plt
import plot_functions as pf
# from collections import Counter
# from string import punctuation

# 1.2: Class Declaration -----------------------------------------------------#
class image_file: 
    
    def __init__ (self, filename, file_ext):
        self.filename = filename
        self.extension = file_ext
        self.image_data = PIL.Image.open(filename)
        self.image_array = np.array(self.image_data)
    
    def display_image(self):
        self.image_data.show()
        
    def return_array(self):
        return self.image_array
    
#----------------------------------- START -----------------------------------#
#----------------------- PHASE 2: Program Execution --------------------------#
#-----------------------------------------------------------------------------#
        
laptop = image_file('laptop.jpg', 'jpg') # import 'laptop.jpg' file in local directory
laptop.display_image() # display the image

laptop_array = laptop.return_array()

