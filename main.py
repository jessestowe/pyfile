import pyfile

def main():	
	newFile = pyfile.liveFile("testIO", mode="r+")
	input("press enter to continue")
	output = newFile.read()
	print(output)

if __name__ == "__main__":
	main()
