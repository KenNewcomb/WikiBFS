# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""

### WikiBFS: Performs a breadth-first-search on a wikipedia entry to find a keyword.

import sys
import bfs

result = ""
def usage():
	print("Usage: run.py <keyword> <wikipedia page url>")

# Parse user input (run.py microsoft https://en.wikipedia.org/Apple)
if len(sys.argv) is not 3:
	usage()
	sys.exit(0)
else:
	keyword = sys.argv[1]
	wikipage = sys.argv[2]
	result = bfs.bfs(keyword, wikipage)

print("Found keyword " + keyword + " within " + result.getUrl())
print("Level: " + str(result.getLevel()))

if result.getParentList is not []:
	print("Previous clicks:")
	for website in result.getParentList():
		print(website)
