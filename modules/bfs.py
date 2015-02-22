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
	# Enforce a maximum number of threads.
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
	# Display the minimum distance to the keyword.
	print("Found!\n")
	print("Minimum distance: (" + str(page.getLevel()) + " clicks)")
	
	# Gather the list of websites that were clicked on
	urls = page.getParentList()
	urls.append(page.getUrl())
	
	# Pretty formatting.
	hyphencount = 1
	for website in urls:
		for count in range(0, hyphencount):
			print("-", end="", flush=True)
		if count != 0: 
			print("> ",  end="", flush=True)
		print(website)
		hyphencount += 3
	
	# The program hangs for a few seconds at the end while it kills active threads.
	print("Killing leftover threads, just a second...")			

def bfs(page, keyword):
	"""A recursive breadth-first search function"""
	# Recursive, relies on a few global variables
	global found, currentlevel, active_threads, max_threads, active_parents
	
	# If the keyword has been found, kill the thread
	if found is True:
		return

	# Mark the URL as visited
	visited.append(page.getUrl())
	
	# Get HTML from URL
	pageHTML = urltoHTML(page.getUrl())
	
	# Get page text from HTML
	pagetext = pageHTML.get_text()
	
	# Let the user know if a new level is reached.
	if page.getLevel() > currentlevel:
		currentlevel += 1
		print("Scanning hyperlinks on level " + str(currentlevel) + ".")
	
	# Scan the page for the keyword; if found, end the search.
	if keyword in pagetext:
		found = True
		printOutput(page)
		return
		
	# Build list of parents.
	parentlist = copy.deepcopy(page.getParentList())
	parentlist.append(page.getUrl())
	active_parents.append(page.getLevel())
	
	# Build list of children (URLS on the page)
	for link in pageHTML.find_all("a", href=True):
		# If the url hasn't been visited, is an internal link, isn't an anchor, etc...
		if baseurl + link['href'] not in visited and link['href'].startswith("/wiki") and "#" not in link['href'] and ":" not in link['href']:
			url = baseurl + link['href'] # Add the baseurl since it is a relative link
			while True:
				if found is True:
					return
				if active_threads <= max_threads and min(active_parents) >= page.getLevel():
					t = threading.Thread(target=bfs, args = (Page(url, page.getLevel() + 1, parentlist),keyword))
					t.start()
					break
				time.sleep(0.3)
				
	active_parents.pop(active_parents.index(page.getLevel()))
