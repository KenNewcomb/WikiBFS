# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""
from bs4 import BeautifulSoup
import requests
import Queue

def urltoHTML(wikipage):
        """Generates a BeautifulSoup page and pagetext for a given URL"""
        # Get the html using Requests
        html = requests.get(wikipage).content

        # Feed the html into BeautifulSoup
        page = BeautifulSoup(str(html))

        # Get the text from the page.
        pagetext = page.get_text()

        return (page, pagetext)

def bfs(keyword, wikipage):
        """Performs a breadth first search"""
	# Create a queue of nodes to be visited and a list of wikipedia pages to the target.
	pagequeue = Queue.Queue()
	path = []
	
	# Generate initial BS page object and page text.
	(page, pagetext) = urltoHTML(wikipage)

	while(pagequeue.qsize() is not 0):
        	# Check to see if the keyword is in page's text.
        	if keyword in pagetext:        
        		return(wikipage)
	
		urllist = []
		# Find all urls
		for link in page.find_all("a"):
			urllist.append(link.get('href'))
	
		for url in urllist:
			for website in pagequeue:
				if url not in pagequeue:
					path.append(url)
					pagequeue.put(url)
	return None
