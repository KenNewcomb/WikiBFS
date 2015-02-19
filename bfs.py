# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""
from bs4 import BeautifulSoup
import copy
import requests
import Queue
from classes.page import Page
import time
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
	pagequeue.put(Page(wikipage, 0, []))
	
	currentLevel = 0
	while(pagequeue.qsize() is not 0):
		# Dequeue next page
		currentpage = pagequeue.get()
		
		# Check if queue is part of next generation of links
		if currentpage.getLevel() > currentLevel:
			currentLevel += 1
			print("Scanning hyperlinks on level " + str(currentLevel) + ".")
		# Set page as visited
		visited.append(currentpage.getUrl())
		# Get HTML from URL
		pageHTML = urltoHTML(currentpage.getUrl())
		
		# Get page text from HTML
		pagetext = pageHTML.get_text()		

        	# Check to see if the keyword is in page's text.
        	if keyword in pagetext:
			return currentpage
	
		# Build list of parents
		parentlist = copy.deepcopy(currentpage.getParentList())
		parentlist.append(currentpage.getUrl())

		# Find all urls
		for link in pageHTML.find_all("a", href=True):
			if baseurl + link['href'].encode('utf-8') not in visited and link['href'].encode('utf-8').startswith("/wiki") and ("#" not in link['href'].encode('utf-8')) and (":" not in link['href'].encode('utf-8')):
				url = baseurl + link['href']
				visited.append(url)
				pagequeue.put(Page(url, currentpage.getLevel() + 1, parentlist))
	return None
