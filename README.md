WikiBFS
=======

Given a Wikipedia article URL and a keyword, WikiBFS performs a [breadth-first search](https://en.wikipedia/wiki/Breadth-first_search) to find the given search query. WikiBFS first searches the given Wikipedia page for the query string. If the string is not found, it then searches every hyperlink on the page. The algorithm continues until the keyword is found.

Usage
------

	python run.py <keyword> <wikipedia page URL>

Example
-------

Let's try to find the word "entropy", starting with the Wikipedia page for a Kiwi. 

	python run.py entropy https://en.wikipedia.org/wiki/Kiwi

	Locating entropy...
	Scanning hyperlinks on level 1.
	Scanning hyperlinks on level 2.
	Found!
	
	Minimum Path: (2 clicks)
	https://en.wikipedia.org/wiki/Ethylene
	- - - >  https://en.wikipedia.org/wiki/Kiwifruit
	- - - - - - >  http://en.wikipedia.org/wiki/Kiwi

There you have it! It followed two links to find "entropy", clicking on "Kiwifruit" and then "Ethylene". 

Have fun!
