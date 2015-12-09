# pyfile  
A python utility for reading and writing files as objects  
  
NOTE:  
1. Written for python 3. Funtionality is unknown for python 2.  
2. main.py contains a simple tutorial which goes over the basic  
	functionality of the library.  
  
TO USE:  
1. import the pyfile in a python script.    
2. You can create a new file by calling pyfile.liveFile()  
	with the path to the file as the first argument.  
	All other arguments are optional  
3. calling liveFile.read() will read the file, and will  
	always return a complete and up to date version of  
	the file.  
4. calling liveFile.write() will append to the file.  
	If a change has been detected since the last read,  
	then an IOError is thrown warning of the change. This  
	can be over ridden by passing in overRide=True as the  
	second argument to write.  
