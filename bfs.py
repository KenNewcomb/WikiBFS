# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:22:53 2015

@author: kentropy
"""
from bs4 import BeautifulSoup
def bfs(keyword, wikipage):
        """Performs a breadth first search"""
        page = BeautifulSoup(wikipage)

        # Check to see if word is in page's text. If so, bfs is finished.
        pagetext = page.get_text()
        if keyword in pagetext:
                print("Page found")