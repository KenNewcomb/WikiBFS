# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""
from bs4 import BeautifulSoup
import requests

def bfs(keyword, wikipage):
        """Performs a breadth first search"""
	# Get the html using Requests
	html = requests.get(wikipage).content
	# Feed the html into BeautifulSoup
        page = BeautifulSoup(str(html))
	# Get the text from the page.
	pagetext = page.get_text()

        # Check to see if the keyword is in page's text.
        if keyword in pagetext:
                return "FOUND IT"
	else:
		# Construct a list of urls to visit next.
		urllist = []
		
