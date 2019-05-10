Security Algorithms Steganography Project
====================


# SETUP:
There are a few dependencies needed , I have included steghide in the parent directory. I have also included an a condaEnv.yaml file you can use to create a mirror of my conda environment. You will need to change the prefix and name if you so choose.

An "Empty" pictures directory exists under StegProject. This is where all pictures you use to hide your text file in will be stored.
Ensure you delete the Deleteme file from within the pictures directory and add in the pictures you wish to use. 

A sample secrets.txt has been provided as an example but you must create a file which contains a CSV in the following
order
<AES_KEY>,<AES_INITIAL_VECTOR>,<STEGHIDE_PASSWORD>


# How to use
run `python main.py` You will be prompted for the secret file path. 

From here choose your options. 

## Option 1
- After option 1 will ask you for a file, for example there bob.txt provided. 
- THIS HAS WORKED IN SMALL TESTS WITH PICTURES 
- You will then be asked what port you want to serve on.
- Then a simple web server will spin up hosting your images with in this case holds bob.txt's data

## Option 2
- Provide the ip address(in the case of running locally localhost is fine)
- Provide the port number the web server is using.
- Provide the name of the extracted file, the decrypted version will be the provided name with the suffix '.decrypt' 
- It will then scrape the web page for images and then extract your txt files contents out.
 
## Option 3
- Provides you with a rough estimate of the size file you can store in your pictures.



# common errors:
- If you are getting permission errors, ensure you have write permission to the StegProject directory
- This is only tested on windows. 
- Very little testing on image encryption. 
