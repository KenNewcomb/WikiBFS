# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""

### WikiBFS: Performs a breadth-first-search on a wikipedia entry to find a keyword.

import sys
import bfs

def usage():
	print("Usage: run.py <keyword> <wikipedia page url>")

# Parse user input (run.py microsoft https://en.wikipedia.org/Apple)
if len(sys.argv) is not 3:
	usage()
else:
	keyword = sys.argv[1]
	wikipage = sys.argv[2]
	result = bfs.bfs(keyword, wikipage)

# Scrape wikipedia entry text for all links.
def bfs(keyword, wikipage):
	"""Performs a breadth first search"""
	page = BeautifulSoup(wikipage)
	
	# Check to see if word is in page's text. If so, bfs is finished.
	pagetext = page.get_text()
	if keyword in pagetext:
		print("Page found")
	

