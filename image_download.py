#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:50:23 2020

@author: patrickbenitez
"""

# Environment Setup  -----------------------------#

import requests
import os

from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


# Function Declaration  -----------------------------#

def is_valid(url):
    """
    Purpose: validate URLs
    """
    
    parsed_url = urlparse(url)
    
    return bool(parsed_url.netloc) and bool (parsed_url.scheme)

def get_all_images(url):
    """
    Purpose: returns all image URLs on a single 'url"
    """
    
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        # make the URL absolute by joining domain with the URL that is just extracted
        img_url = urljoin(url, img_url)
        # remove URLs like '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # finally, if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls


    
def download(url, pathname):
    """
    Purpose: downloads a file given an URL
    """
    
    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    # download the body of response        
    response = requests.get(url, stream = True)
    
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    
    # progress bar
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    
    with open(filename, "wb") as f:
        for data in progress:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))
            
def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
        # for each image, download it
        download(img, path)
        
main("https://www.thepythoncode.com/topic/web-scraping", "image_web_scrape")
    