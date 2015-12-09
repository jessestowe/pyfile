import io
import os
import time

class liveFile(io.FileIO):
	
	def getTimestamp(self):
		return os.path.getmtime(self.path)

	def _getContents(self):
		self.seek(0)
		return super().read().decode()

	def __init__(self, name, mode="rw", closefd=True, opener=None):
		super().__init__(name, mode, closefd, opener)
		self.path = name
		self.opener = opener
		self.timestamp = self.getTimestamp()
		self.contents = self._getContents()
	
	def isCurrent(self):
		return (self.getTimestamp() == self.timestamp)

	def read(self):
		if not self.isCurrent():
			self.close()
			self.__init__(self.name, self.mode, self.closefd, self.opener)
		return self.contents

	def write(self, value):
		if not self.isCurrent():
			self.close()
			self.__init__(self.name, self.mode, self.closefd, self.opener)
		self.write(value)
		
