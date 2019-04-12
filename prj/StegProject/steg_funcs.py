import subprocess
import os, signal, time


def call_process(command):
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	out, err = process.communicate()
	process.wait()
	return out


def steg_info(filenames):
	sizes = []
	for s in filenames:

		process = subprocess.Popen(["steghide\steghide.exe", "info", "pictures/" + s], stderr=subprocess.STDOUT,
		                           stdout=subprocess.PIPE, stdin=subprocess.PIPE)
		out, err = process.communicate(b'n')
		infoarray = str(out).split()
		#This whole if/else is terrible and will be changed up.
		if infoarray[5] == "KB":
			#needs major testing
			sizes.append(int(float(infoarray[18]) * 1024) - 100)
		else:
			sizes.append(int(float(infoarray[18])) - 100)
	return sizes



def steg_version():
	return call_process(["steghide\steghide.exe", "--version"])


#untested
def md5_pass(file):
	return str.split(call_process(["md5sum", file]))[0]


def steg_hide(files_to_hide, files_to_use, password):
	print(files_to_hide)
	print(files_to_use)
	for h, u in zip(files_to_hide, files_to_use):
		print(call_process(["steghide\steghide.exe", "embed", "-ef", str(h), "-cf", "pictures/" + u, "-p", password]))
		os.remove(str(h))


def steg_read(files_to_read, password):
	filesarray = []
	for s in files_to_read:
		call_process(["steghide\steghide.exe", "extract", "-xf", "temp", "-sf", s, "-p", password, "-f"])
		extracted_file = open("temp", "r")
		filesarray.append(extracted_file.read())
		extracted_file.close()
		os.remove("temp")
		os.remove(s)
	return filesarray


# reads images into an array from the image file
def read_images():
	return os.listdir("pictures/")


# joins the file parts back together- not really needed.
def join_files(file_parts):
	outfile = open("DECRYPTED", "w")
	for i in file_parts:
		outfile.write(i)
		#outfile.write(i.read())


# returns an array of the file names written
def split_file(file_to_read, sizearray):
	readbytes = 0
	infile = open(file_to_read)
	files_written = []

	for i in sizearray:
		# we're naming the file the read bytes
		outfile = open(str(readbytes), "w+")
		outfile.write(str(bytearray(infile.read(i), 'utf-8')))
		files_written.append(readbytes)
		readbytes += i
	return files_written

