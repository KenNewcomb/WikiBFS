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
	path = bfs.bfs(keyword, wikipage)
