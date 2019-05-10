"""
Method to contain all steghide calls.
@author Troy Flagg
"""
import os
import subprocess


class StegHide:
    """
    Wrapper class to contain all steghide and systemcall methods.
    """

    def call_process(self, command):
        """
        Create a helper method for calling subprocesses
        :return:
        """
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        out, err = process.communicate()
        process.wait()
        return out

    def steg_info(self, filenames):
        """
        Generates steganography file info for how much data each image can hold.
        :return : array of sizes each picture can hold.
        """
        sizes = []
        for s in filenames:
            process = subprocess.Popen(["steghide\steghide.exe", "info", "pictures/" + s], stderr=subprocess.STDOUT,
                                       stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            out, err = process.communicate(b'n')

            # Split the ugly output to everything after capacity
            size_info = str(out).split('capacity: ', 1)[1]
            # Further split the string to look like [<size>, <KB/Bytes>]
            size_info = size_info.split(' ', 1)
            # We are trying to return everything in bytes, so if its KB, multiply by 1024
            if size_info[1].startswith('KB'):
                sizes.append(int(float(size_info[0]) * 1024) - 100)
            elif size_info[1].startswith('Byte'):
                sizes.append(int(float(size_info[0])) - 100)
        return sizes

    def steg_version(self):
        """
        Returns the Steghide version.
        :return: Steghide version
        """
        return self.call_process(["steghide\steghide.exe", "--version"])

    def md5_pass(self, file):
        """
        Used to show the md5_sum changes as we encode thigns into images
        :param file: file to check md5_sum
        :return: md5sum.
        """
        return str.split(self.call_process(["md5sum", file]))[0]

    def steg_hide_many(self, files_to_hide, files_to_use, password):
        """
        The method called when an encrypted .txt must be split across many pictures.
        :param files_to_hide: The split encrypted .txt
        :param files_to_use: The pictures to hide files_to_hide
        :param password: The steghide password.
        :return:
        """

        for h, u in zip(files_to_hide, files_to_use):
            self.call_process(
                    ["steghide\steghide.exe", "embed", "-ef", str(h), "-cf", "pictures/" + u, "-p", password])
            os.remove(str(h))

    def steg_hide(self, file_to_hide, file_to_use, password):
        self.call_process(
            ["steghide\steghide.exe", "embed", "-ef", file_to_hide, "-cf", "pictures/" + file_to_use, "-p", password])

    def steg_read(self, files_to_read, password):
        """
        :param files_to_read:
        :param password:
        :return:
        """
        filesarray = []
        for s in files_to_read:
            self.call_process(["steghide\steghide.exe", "extract", "-xf", "temp", "-sf", s, "-p", password, "-f"])
            extracted_file = open("temp", "rb")
            filesarray.append(extracted_file.read())
            extracted_file.close()
            os.remove("temp")
            os.remove(s)
        return filesarray

    def read_images(self):
        """
        Reads the images into an array
        :return:
        """
        return os.listdir("pictures/")

    def join_files(self, file_parts, file_name):
        """
        When we split files initially we will eventually need to bring them back together.
        :param file_parts: The array containing all of the file parts.
        :param file_name: The file to write to.
        :return:
        """

        outfile = open(file_name, "wb")
        for i in file_parts:
            outfile.write(i)


    def split_file(self, file_to_read, sizearray):
        """
        The method used when we have to split a file into many smaller files to hide in pictures
        :param file_to_read: The initial file we are encrypting
        :param sizearray: The array of the containment size of each picture we are going to use.
        :return: The list of smaller files to fit into pictures.
        """
        readbytes = 0
        infile = open(file_to_read, 'rb')
        files_written = []

        for i in sizearray:
            # we're naming the file the read bytes
            outfile = open(str(readbytes), "wb")
            outfile.write(infile.read(i))
            files_written.append(readbytes)
            readbytes += i
        return files_written
