class Page:
	
	url = ""
	level = 0
	parentlist = []

	def __init__(self, url, level, parentlist):
		self.url = url
		self.level = level
		self.parentlist = parentlist

	def getUrl(self):
		return self.url

	def getLevel(self):
		return self.level
	
	def getParentList(self):
		return self.parentlist
