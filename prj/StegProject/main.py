"""
Main method to encrypt a .txt file with varying levels of AES encryption and encode into an image to host
and to download.
@author Troy Flagg
"""
import steganography
import webmethods
import encryption

# Define some constants here
SERVER_CHOICE = '1'
CLIENT_CHOICE = '2'
STEG_INFO_CHOICE = '3'
KEY_LOCATION = 0
IV_LOCATION = 1
STEG_PASS_LOCATION = 2
MAX_CSV_LENGTH = 3

operation = input("Enter the name of a file containing your AES Key, Init Vector and Steghide password: ")
try:
	fh = open(operation, 'r')
	secrets = fh.readline()
	secrets = secrets.split(',')
	if len(secrets) is MAX_CSV_LENGTH:
		key = secrets[KEY_LOCATION]
		IV = secrets[IV_LOCATION]
		steg_pass = secrets[STEG_PASS_LOCATION]
	else:
		print('Your Secret file had less than 3 elements in the CSV, check it and ensure that it follows the '
		      'following format: <key>,<IV>,<Steghide Password>')
except FileNotFoundError:
	print('Your given file does not exist or the file path is wrong.')
	exit()

crypto = encryption.CryptoMethods(key, IV)


operation = input("Serve(1), Recieve(2), or Check Space(3)")

if operation == SERVER_CHOICE:
	webmethods.server(crypto, steg_pass)
if operation == CLIENT_CHOICE:
	webmethods.client(crypto, steg_pass)
if operation == STEG_INFO_CHOICE:
	steg = steganography.StegHide()
	files = steg.read_images()
	file_sizes = steg.steg_info(files)
	# total room in pictures folder
	totalbytes = sum(file_sizes)
	print(str(totalbytes) + " bytes, or about " + str(round(float(totalbytes) / 1024, 2)) + " KB")
else:
	print("Incorrect Choice, enter 1 for Server, 2 for Client or 3 to check the space in your pictures directory")
	exit()
