# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""

### WikiBFS: Performs a breadth-first-search on a wikipedia entry to find a keyword.

import sys
from modules import bfs
from classes.page import Page

def usage():
	"""Prints the program instructions to the screen"""
	print("Usage: run.py <keyword> <wikipedia page url>")

# Parse user input (run.py microsoft https://en.wikipedia.org/Apple)
if len(sys.argv) is not 3:
	usage()
	sys.exit(0)
else:
	# Get keyword and url from launch parameters
	keyword = sys.argv[1]
	url = sys.argv[2]
	
	# Let the user know the search has begun
	print("Locating " + keyword + "...")
	sys.stdout.flush()
	
	# Start the search
	bfs.bfs(Page(url, 0, []), keyword)
