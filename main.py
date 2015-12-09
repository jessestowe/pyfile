import pyfile

def main():	
	newFile = pyfile.liveFile("testIO", mode="r+")
	input("press enter to continue")
	print(newFile.read())

if __name__ == "__main__":
	main()
