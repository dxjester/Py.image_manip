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


class image_file: 
    
    def __init__ (self, filename, file_ext):
        self.filename = filename
        self.extension = file_ext
        self.image_data = PIL.Image.open('laptop.jpg')
        self.image_array = np.array(self.image_data)
    
    def return_array():
        