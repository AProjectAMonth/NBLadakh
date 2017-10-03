# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.shortcuts import render
from urllib.request import urlopen

from django.shortcuts import render

# Create your views here.

class Image():
	def __init__(self, captiontext, url, username, likes_count, img_id):
		self.captiontext = captiontext
		self.url = url
		self.username = username
		self.likes_count = likes_count
		self.img_id = img_id

def extract_data(url):
    response = urlopen(url)
    return json.loads(response.read().decode())

def home(request):
    img = list()
    url = 'https://www.instagram.com/nbladakh/media'
    data = extract_data(url)

    for item in data['items']:
        std_url = item['images']['standard_resolution']['url']
        hd_url = std_url.replace("s640x640","s1080x1080")
        captiontext = item['caption']['text']
        username = item['caption']['from']['username']
        likes_count = item['likes']['count']
        img_id = item['id']
        img_instance = Image(captiontext, hd_url, username, likes_count, img_id)
        img.append(img_instance)

    while(data["more_available"] is True):
	    if data["more_available"] is True:
	        max_id = data["items"][-1]["id"]
	        url = url + "?max_id=" + max_id
	        data = extract_data(url)

	        for item in data['items']:
		        std_url = item['images']['standard_resolution']['url']
		        hd_url = std_url.replace("s640x640","s1080x1080")
		        captiontext = item['caption']['text']
		        username = item['caption']['from']['username']
		        likes_count = item['likes']['count']
		        img_id = item['id']
		        img_instance = Image(captiontext, hd_url, username, likes_count, img_id)
		        img.append(img_instance)

    print(len(img))
    context = {
        "images" : img, 
    }

    return render(request, 'index.html', context)
