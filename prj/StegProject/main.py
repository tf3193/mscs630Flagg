import steganography
import webmethods
import os


# I do some bad stuff here of encoding and dumb decoding.
def server():
	print("Running as Server")
	filename =input("What file do you want to serve?: ")
	files = steg.read_images()
	# array of image holding capacity
	file_sizes = steg.steg_info(files)
	# total room in pictures folder
	total_room = sum(file_sizes)
	infile = open(filename)
	# gets the file size
	infile.seek(0,2) # move the cursor to the end of the file
	size = infile.tell()
	print("File is "+ str(size) + " bytes, and total room is " + str(total_room))
	if total_room < size:
		print("Not enough space")
		exit(1)
	# now the file needs to be split and encoded into images
	size_sum = 0
	index = 0
	while size_sum<size:
		size_sum+=file_sizes[index]
		index+=1
	
	splitarray = file_sizes[:index]
	picstoencode = files[:index]
	splitfiles = steg.split_file(filename, splitarray)
	#the actual process of encoding the files into the images
	steg.steg_hide(splitfiles, picstoencode,"password")
	web.generate_index(picstoencode)
	web.start_http()
	exit(0)	
	

def client():
	print("Running as client")
	target_IP = input("Enter target IP: ")
	imgarray = web.download_imgs(target_IP)
	filesarray = steg.steg_read(imgarray, "password")
	steg.join_files(filesarray)
	exit(0)

steg = steganography.StegHide()
web = webmethods.webHostAndScraper()


operation = input("Serve(1), Recieve(2), or Check Space(3) DONT PICK 3 it will blow things up: ")


if operation == "1":
	server()
if operation == "2":
	client()
if operation == "3":
	files = steg.read_images()
	file_sizes = steg.steg_info(files)
	# total room in pictures folder
	totalbytes = sum(file_sizes)
	print(str(totalbytes) + " bytes, or about " + str(round(float(totalbytes)/1024, 2)) + " KB")
	
else:
	print("Incorrect Choice")
	exit()
