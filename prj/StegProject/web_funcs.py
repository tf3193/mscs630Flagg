import http.server
import socketserver
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import os

from html.parser import HTMLParser

#Globals are fun.
global boo
boo = []

class webHostAndScraper:

	def start_http():
		PORT = 8000

		Handler = http.server.SimpleHTTPRequestHandler

		httpd = socketserver.TCPServer(("", PORT), Handler)

		print("Serving at port", PORT)
		httpd.serve_forever()


	def generate_index(string_array):
		os.remove("index.html")
		myfile = open("index.html", "a")
		for s in string_array:
			myfile.write("<IMG SRC=pictures/" + s + ">" + "\n")


	class MyHTMLParser(HTMLParser):
		def handle_starttag(self, tag, attrs):
			for attr in attrs:
				boo.append(attr[1].split("/")[1])


	def download_imgs(ip_addr):
		urlobj = urllib.request.urlopen("http://" + ip_addr + ":8000")
		web_pg = str(urlobj.read())
		parser = MyHTMLParser()
		parser.feed(web_pg)
		imgsarray = []
		# loops over the gathered image names and downloads them
		for s in boo:
			urllib.request.urlretrieve("http://" + ip_addr + ":8000/pictures/" + s, s)
			imgsarray.append(s)
		return imgsarray
