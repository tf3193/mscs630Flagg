Security Algorithms Steganography Project
====================


#HOW TO RUN:
create a "pictures" directory under src. This is where all pictures you use to hide your text file in will be stored.

run `python main.py` and choose your options.

#### Option 1
- After option 1 will ask you for a file, for example there bob.txt provided. 
- Then a simple web server will spin up hosting your images with in this case holds bob.txt's data

#### Option 2
- Provide the ip address(in this case it is localhost)
- It will then scrape the web page for images and then extract your txt files contents out. 

#### Option 3
- Does not work, do not use. 
- In future it will give you a size that is available to hide your .txt file in. 


#common errors:
- if there are string conversion errors somewhere in steg_funcs.py, it probably means that 
 a file that isn't a picture exists in your pictures folder.

- many more....