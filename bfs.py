# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""
from bs4 import BeautifulSoup
import requests
import Queue

baseurl = "https://en.wikipedia.org"

def urltoHTML(wikipage):
        """Generates a BeautifulSoup page and pagetext for a given URL"""
        # Get the html using Requests
        html = requests.get(wikipage).content

        # Feed the html into BeautifulSoup
        page = BeautifulSoup(str(html))

        return(page)

def bfs(keyword, wikipage):
        """Performs a breadth first search"""
	# Create a queue of nodes to be visited and a list of wikipedia pages to the target.
	pagequeue = Queue.Queue()
	visited = []
	# Generate initial BS page object and page text.
	pagequeue.put((wikipage, 0))
	
	last_depth = 0
	while(pagequeue.qsize() is not 0):
		# Dequeue next page
		(page, depth) = pagequeue.get()

		# Get HTML from URL
		pageHTML = urltoHTML(page)
		
		# Get page text from HTML
		pagetext = pageHTML.get_text()		
	
        	# Check to see if the keyword is in page's text.
        	if keyword in pagetext:
			print(keyword)
        		print(str(depth) + " " + page)
			print("FOUND")
		
		if depth > last_depth: 
			last_depth += 1 
			print(str(depth) + " " + page)
		urllist = []

		# Find all urls
		for link in pageHTML.find_all("a", href=True):
			if link['href'].encode('utf-8').startswith("/"):
				url = baseurl + link['href']
				urllist.append(url)
	
		for url in urllist:
			if url not in visited:
				visited.append(url)
				pagequeue.put((url, depth+1))
	return None
