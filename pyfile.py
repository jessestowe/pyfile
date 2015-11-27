import io
import os

class liveFile(io.FileIO):
	
	def __init__(self, name, mode='r', closefd=True, opener=None):
		super().__init__(self, name, mode, closefd, opener)
		self.contents = None
		self.timestamp = None
