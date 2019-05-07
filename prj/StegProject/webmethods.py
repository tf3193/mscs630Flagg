import http.server
import os
import socketserver
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser


class webHostAndScraper:
	"""
	Class to contain all web methods.
	"""
	imageList = []

	def start_http(self):
		"""
		Method to start the http server on port 8000
		:return:
		"""
		PORT = 8000
		handler = http.server.SimpleHTTPRequestHandler
		httpd = socketserver.TCPServer(("", PORT), handler)
		print("Serving at port", PORT)
		httpd.serve_forever()

	def generate_index(self, string_array):
		"""
		Generates the index.html file to serve
		:param string_array:
		:return:
		"""
		os.remove("index.html")
		myfile = open("index.html", "a")
		for s in string_array:
			myfile.write("<IMG SRC=pictures/" + s + ">" + "\n")

	class MyHTMLParser(HTMLParser):
		"""
		Override the handle_starttag method in htmlparser to scrape for images on the web page.
		"""
		def handle_starttag(self, tag, attrs):
			for attr in attrs:
				self.imageList.append(attr[1].split("/")[1])

	def download_imgs(self, ip_addrress):
		"""
		Downloads images that are hosted at the given ip address on port 8000
		:param ip_addrress:
		:return a list of images:
		"""
		urlobj = urllib.request.urlopen("http://" + ip_addrress + ":8000")
		web_pg = str(urlobj.read())
		parser = self.MyHTMLParser()
		parser.feed(web_pg)
		imgsarray = []
		# loops over the gathered image names and downloads them
		for s in self.imageList:
			urllib.request.urlretrieve("http://" + ip_addrress + ":8000/pictures/" + s, s)
			imgsarray.append(s)
		return imgsarray
