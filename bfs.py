# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""
from bs4 import BeautifulSoup
import copy
import requests
import queue
from classes.page import Page
import threading
import time

baseurl = "https://en.wikipedia.org"
found = False
visited = []
currentlevel = 0
max_threads = 30	
active_threads = 0
num_urls = 0
active_parents = []

def urltoHTML(wikipage):
	global active_threads
	active_threads += 1
	"""Generates a BeautifulSoup page and pagetext for a given URL"""
	# Get the html using Requests
	#print("Requesting wikipage:   " + wikipage)
	html = requests.get(wikipage).content

	# Feed the html into BeautifulSoup
	page = BeautifulSoup(str(html))
	#print("Page received:   " + wikipage)
	active_threads -= 1
	return(page)
	
def printOutput(page):
	"""Prints output"""
	print("Found!\n")
	print("Minimum Path: (" + str(page.getLevel()) + " clicks)")
	hyphencount = 1
	urls = page.getParentList()
	urls.append(page.getUrl())
	for website in urls:
		for count in range(0, hyphencount):
			print("-", end="", flush=True)
		print("> ",  end="", flush=True)
		print(website)
		hyphencount += 3
			

def bfsrecur(page, keyword):
	global found, currentlevel, active_threads, max_threads, active_parents
	if found is True:
		return

	visited.append(page.getUrl())
	# Get HTML from URL
	pageHTML = urltoHTML(page.getUrl())
	# Get page text from HTML
	pagetext = pageHTML.get_text()
	
	if page.getLevel() > currentlevel:
		currentlevel += 1
		print("Scanning hyperlinks on level " + str(currentlevel) + ".")
	
	if keyword in pagetext:
		found = True
		printOutput(page)
		
	# Build list of parents
	parentlist = copy.deepcopy(page.getParentList())
	parentlist.append(page.getUrl())
	active_parents.append(page.getLevel())
	# Find all urls
	for link in pageHTML.find_all("a", href=True):
		if baseurl + link['href'] not in visited and link['href'].startswith("/wiki") and "#" not in link['href'] and ":" not in link['href']:
			url = baseurl + link['href']
			visited.append(url)
			while True:
				if found is True:
					return
				if active_threads <= max_threads and min(active_parents) >= page.getLevel():
					t = threading.Thread(target=bfsrecur, args = (Page(url, page.getLevel() + 1, parentlist),keyword))
					t.start()
					break
				time.sleep(0.5)
				
	active_parents.pop(active_parents.index(page.getLevel()))
			
def bfs(keyword, wikipage):
	"""Performs a breadth first search"""
	# Create a queue of nodes to be visited and a list of wikipedia pages to the target.
	pagequeue = queue.Queue()
	

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
			linklist = []
			if baseurl + link['href'] not in visited and link['href'].startswith("/wiki") and "#" not in link['href'] and ":" not in link['href']:
				url = baseurl + link['href']
				visited.append(url)
				
	return None	