import requests
import urllib.parse
import os
import re
import json
import random
import warnings

from bs4 import BeautifulSoup
from cs50 import SQL
from imgurpython import ImgurClient
from flask import Flask, jsonify, render_template, request
from flask import current_app as app

def createTable(number):
    """Returns game-table as shuffled list of image-links, checks if imgur is down"""
    image_list = getimgur(number)
    if None in image_list or len(image_list) < number:
        return createBasicTable(number)
    else:
        return createImgurTable(image_list)


def createBasicTable(number):
    """Creates shuffled list for game-table with local image-links"""
    images = []
    for e in range(1,number + 1):
        images.append("static/images/" + str(e) + ".jpg")
        images.append("static/images/" + str(e) + "-.jpg")
    shuffled = random.sample(images, len(images))
    return shuffled


def createImgurTable(image_list):
    """Creates shuffled list for game-table with imgur image-links"""
    images = []
    for e in image_list:
        images.append(e)
        images.append(e + "-")
    shuffled = random.sample(images, len(images))
    return shuffled


def getimgur(number):
    """Get list of imgur image-links"""
    images = []

    # ensure api keys are set
    API_KEY, API_SECRET = apiKeys()

    if not API_KEY:
        warnings.warn("API_KEY not set")
    if not API_SECRET:
        warnings.warn("API_SECRET not set")
        return images

    client = ImgurClient(API_KEY, API_SECRET)
    get_images = client.memes_subgallery(sort='viral', page=0, window='week')

    for image in get_images:
        if responseOk(image.link) == True:
            if image.link is not None:
                if len(images) < number:
                    images.append(image.link)
                else:
                    return images
        else:
            for e in imgurScrape(image.link):
                if e is not None:
                    if len(images) < number:
                        images.append(e)
                    else:
                        return images
    return images


def responseOk(link):
    """Checks if imgur link is direct image link """
    r = requests.request('GET', link + '.extension')
    if r.status_code == 200:
        return True
    else:
        return False


def imgurScrape(link):
    """Scrapes imgur page for images"""
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    image_lists = soup.find_all(itemprop='contentURL')
    imgs = [ x.get('src') for x in image_lists]
    return imgs


def apiKeys():
    API_KEY = ""
    API_SECRET = ""

    if 'API_KEY' in app.config and 'API_SECRET' in app.config:
        print("variable in config")
        API_KEY = app.config['API_KEY']
        API_SECRET = app.config['API_SECRET']
    elif 'API_KEY' in os.environ and 'API_SECRET' in os.environ:
        API_KEY = os.environ.get('API_KEY')
        API_SECRET = os.environ.get('API_SECRET')
    return API_KEY, API_SECRET