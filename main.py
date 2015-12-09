import pyfile

def main():	
	file = "testIO"
	print("Welcome. This is a demonstration of the pyfile library")
	print("Opening {} file".format(file))
	newFile = pyfile.liveFile(file)
	print("Contents of file are:\n")
	output = newFile.read()
	print(output)
	print("Now open a new terminal and make a change to {}".format(file))
	input("Press enter when complete")
	print("Contents of file are:\n")
	output = newFile.read()
	print(output)
	print("changes were automatically detected and refreshed in the file object")
	fileInput = input("Now enter some text to write to the file:")
	newFile.write(fileInput)
	print("Contents of file are:\n")
	output = newFile.read()
	print(output)
	print("File object was automatically opened in write mode and written to")
	print("Now open another terminal again and make another change to {}".format(file))
	input("press enter when complete")
	try:
		newFile.write(fileInput)
	except IOError as e:
		print(e)
		print("\nThe above warning tells us the file has been modified since it's last read. Therefore where we thought we might be writing to may have changed. To write anyway and ignore the message, call write with overRide = True.")
	else:
		print("You didn't make a change to the file, so the file was written to without printing a warning")

	print("This concludes the demonstration. Thanks for using pyfile!")

if __name__ == "__main__":
	main()
