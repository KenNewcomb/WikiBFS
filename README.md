WikiBFS
=======

Given a Wikipedia article URL and a keyword, WikiBFS performs a recursive and parallelized [breadth-first search](https://en.wikipedia.com/wiki/Breadth-first_search) to find the given search query. WikiBFS first searches the given Wikipedia page for the query string. If the string is not found, it then searches every hyperlink on the page. The algorithm continues until the keyword is found.

NOTE: WikiBFS is only supported for Python 3. 


Dependencies
------------

1. BeautifulSoup
2. Requests

Usage
------

	python3 run.py <keyword> <wikipedia page URL>

Example
-------

Let's try to find the word "entropy", starting with the Wikipedia page for a Kiwi (the bird). 

	python3 run.py entropy https://en.wikipedia.org/wiki/Kiwi

	Locating entropy...
	Scanning hyperlinks on level 1.
	Scanning hyperlinks on level 2.
	Found!
	
	Minimum Path: (2 clicks)
	https://en.wikipedia.org/wiki/Kiwi
	- - - >  https://en.wikipedia.org/wiki/Kiwifruit
	- - - - - - >  http://en.wikipedia.org/wiki/Ethylene

There you have it! It followed two links to find "entropy", clicking on "kiwifruit" and then "ethylene". 

Have fun!

Acknowledgements
----------------

Special thanks to [hsidky](https://www.github.com/hsidky/) for his significant contributions to the parallelization of the server requests.
