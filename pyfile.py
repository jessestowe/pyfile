import io
import os
import time

class liveFile(io.FileIO):
	
	def getTimestamp(self):
		return os.path.getmtime(self.path)

	def _getContents(self):
		self.seek(0)
		return super().read().decode()

	def __init__(self, name, mode = "r", closefd=True, opener=None):
		super().__init__(name, mode, closefd, opener)
		self.path = name
		self.opener = opener
		self.timestamp = self.getTimestamp()
		self.contents = self._getContents()
	
	def isCurrent(self):
		return (self.getTimestamp() == self.timestamp)

	def read(self):
		if "r" not in self.mode or not self.isCurrent():
			self._refresh("r")

		return self.contents

	def _refresh(self, mode = "r"):
		self.close()
		self.__init__(self.name, mode, self.closefd, self.opener)

	def write(self, value, overRide=False):
		if not self.isCurrent():
			if not overRide:
				raise IOError("WARNING: File has been modified since last opened. Call with overRide = True to over ride.")
			self._refresh("a")
		elif "a" not in self.mode:
			self._refresh("a")
		if type(value) is bytes:
			super().write(value)
		else:
			super().write(value.encode())
		
