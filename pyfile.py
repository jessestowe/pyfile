import io
import os
import time

class liveFile(io.FileIO):
	
	def getTimestamp(self):
		return os.path.getmtime(self.path)

	def getContents(self):
		self.seek(0)
		return super().read()

	def __init__(self, name, mode='r', closefd=True, opener=None):
		super().__init__(name, mode, closefd, opener)
		self.path = name
		self.timestamp = self.getTimestamp()
		self.contents = self.getContents()
	
	def isCurrent(self):
		return (self.getTimestamp() == self.timestamp)

	def read(self):
		if not self.isCurrent():
			self.contents = self.getContents()
		return self.contents

#	def write(self):
		
