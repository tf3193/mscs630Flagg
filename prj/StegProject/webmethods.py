"""
File to contain web hosting and scraping.
@author Troy Flagg
"""
import http.server
import os
import socketserver
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
import steganography

imageList = []


class WebHostAndScraper:
	"""
	Class to contain all web methods.
	"""

	def __init__(self):
		self.imageList = []

	def start_http(self):
		"""
		Method to start the http server on port 8000
		:return:
		"""
		port = input("What port do you want to server on? ")
		port = int(port)
		handler = http.server.SimpleHTTPRequestHandler
		httpd = socketserver.TCPServer(("", port), handler)
		print("Serving at port", port)
		httpd.serve_forever()

	def generate_index(self, string_array):
		"""
		Generates the index.html file to serve
		:param string_array:
		:return:
		"""
		try:
			os.remove("index.html")
		except:
			print('No Existing index to delete, continuing')
		myfile = open("index.html", "a")
		for s in string_array:
			myfile.write("<IMG SRC=pictures/" + s + ">" + "\n")

	def download_imgs(self, ip_addrress, target_port):
		"""
		Downloads images that are hosted at the given ip address and port
		:param ip_addrress:
		:return a list of images:
		"""
		urlobj = urllib.request.urlopen("http://" + ip_addrress + ":" + target_port)
		web_pg = str(urlobj.read())
		parser = MyHTMLParser()
		parser.feed(web_pg)
		imgsarray = []
		# loops over the gathered image names and downloads them
		for s in imageList:
			urllib.request.urlretrieve("http://" + ip_addrress + ":" + target_port + "/pictures/" + s, s)
			imgsarray.append(s)
		return imgsarray


class MyHTMLParser(HTMLParser):
	"""
	Override the handle_starttag method in htmlparser to scrape for images on the web page.
	"""
	def handle_starttag(self, tag, attrs):
		for attr in attrs:
			imageList.append(attr[1].split("/")[1])


def server(crypto, steghide_password):
	"""
	Method used when the user choses to act as a server. It will deal with the following
	Encrypt Given file
	Split given file if if can't be held in one picture
	Encode the encrypted file into the number of pictures needed.
	It will then host a web server to host the pictures with the encoded .txt file.

	:param crypto: The AES object used to encrypt the file.
	:param steghide_password: The password used to encode with steghide.
	:return:
	"""
	steg = steganography.StegHide()
	web = WebHostAndScraper()

	print("Running as Server")
	filename = input("What file do you want to serve?: ")
	# Encrypt the contents of the file before using steghide.
	filename = crypto.encrypt_file(filename)
	picture_list = steg.read_images()
	# array of image holding capacity
	file_sizes = steg.steg_info(picture_list)
	# total room in pictures folder
	total_room = sum(file_sizes)
	encrypted_file_size = os.stat(filename).st_size

	# Ensure we have enough space in our pictures to hide the encrypted file
	print("File is " + str(encrypted_file_size) + " bytes, and total room is " + str(total_room))
	if total_room < encrypted_file_size:
		print("Not enough space")
		exit(1)

	# Now the file needs to be split and encoded into images

	size_sum = 0
	index = 0
	# This will figure out how many pictures we have to use.
	while size_sum < encrypted_file_size:
		size_sum += file_sizes[index]
		index += 1

	split_array = file_sizes[:index]
	picstoencode = picture_list[:index]

	# If we can't fit our encrypted file into one picture we must split the encrypted file.
	if len(split_array) > 1:
		split_files = steg.split_file(filename, split_array)
		steg.steg_hide_many(split_files, picstoencode, steghide_password)
	else:
		steg.steg_hide(filename, picstoencode[0], steghide_password)

	# the actual process of encoding the files into the images
	web.generate_index(picstoencode)
	web.start_http()
	exit(0)


def client(crypto, steghide_password):
	"""
	Method called when user chooses client mode. This will ask for IP and port to scrape the images and then extract
	the AES encrypted .txt file and decrypt it.
	:param crypto: the AES wrapper class
	:param steghide_password: The password used to extract the .txt from steghide.
	:return:
	"""
	steg = steganography.StegHide()
	web = WebHostAndScraper()
	print("Running as client")
	target_ip = input("Enter target IP: ")
	target_port = input("Enter target PORT: ")
	file_name = input("Enter the name of the file you want to write: ")
	imgarray = web.download_imgs(target_ip, target_port)
	files_array = steg.steg_read(imgarray, steghide_password)
	steg.join_files(files_array, file_name)
	crypto.decrypt_file(file_name)
	exit(0)
