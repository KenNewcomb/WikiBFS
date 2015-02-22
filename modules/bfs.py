"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""
from bs4 import BeautifulSoup
import copy
import requests
from classes.page import Page
import threading
import time

baseurl = "https://en.wikipedia.org" # for the processing of relative urls
found = False
visited = []
currentlevel = 0
max_threads = 20	
active_threads = 0
num_urls = 0
active_parents = []

def urltoHTML(wikipage):
	"""Fetches a BeautifulSoup page and pagetext for a given URL"""
	global active_threads
	active_threads += 1

	# Get the html using Requests
	html = requests.get(wikipage).content

	# Feed the html into BeautifulSoup
	page = BeautifulSoup(str(html))

	active_threads -= 1
	return(page)
	
def printOutput(page):
	"""Print the results of the search to the screen."""
	print("Found!\n")
	print("Minimum Path: (" + str(page.getLevel()) + " clicks)")
	hyphencount = 1
	urls = page.getParentList()
	urls.append(page.getUrl())
	for website in urls:
		for count in range(0, hyphencount):
			print("-", end="", flush=True)
			if count != 0: 
				print("> ",  end="", flush=True)
		print(website)
		hyphencount += 3
	print("Killing leftover threads, just a second...")			

def bfs(page, keyword):
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
		return
		
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
				time.sleep(0.3)
				
	active_parents.pop(active_parents.index(page.getLevel()))