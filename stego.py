#!/usr/bin/env python3
import os
import sys
import binascii
import argparse
from optparse import OptionParser
from core.time_util import TimeUtil

DELIMITER = "//-_-_-//"
ENCODING = "utf-8"

def embed(args):
    targetFile = args[0]
    targetFileName = os.path.basename(targetFile)
    patchedFileName = targetFileName.split(".")[0] + "_patched." + targetFileName.split(".")[1]

    with open(targetFile, "rb") as hostFile, open(patchedFileName, "wb+") as patchedFile:
        patchedFile.write(hostFile.read())
        index = 1
        while index < len(args):
            sourceFile = args[index]
            sourceFileName = os.path.basename(sourceFile)
            print("[*] Trying to embed:",sourceFile,"...")
            with open(sourceFile, "rb") as fileToHide:
                patchedFile.write(binascii.hexlify(bytes(sourceFileName + DELIMITER, ENCODING)))
                patchedFile.write(binascii.hexlify(fileToHide.read()))
                patchedFile.write(binascii.hexlify(bytes(sourceFileName + DELIMITER, ENCODING)))
                print("\033[32m[+] \033[0m",sourceFileName,"\033[32mhidden! \033[0m")
            index += 1

    util = TimeUtil()
    util.setModTime( patchedFileName, util.getModTime(targetFile) )

def extract(args):
    with open(args[0], "rb") as targetFile:
        fileContent = targetFile.read()
        fileContentSplit = fileContent.split(bytes("%%EOF", ENCODING))
        fileContent = fileContentSplit[len(fileContentSplit)-1]
        fileContent = binascii.unhexlify(fileContent.strip())

    if fileContent is None:
        print("\033[31m[-] Something went wrong ... !\033[0m")
        sys.exit

    hiddenFiles = fileContent.split(bytes(DELIMITER, ENCODING))
    fileName = None
    fileContent = None
    for index, element in enumerate(hiddenFiles):
        if index % 2 != 0:
            print("[*] Extracting:",fileName, "...")
            with open(fileName, "wb") as hiddenFile:
                hiddenFile.write(element)
                print("\033[32m[+] \033[0m",fileName,"\033[32mextracted! \033[0m")            
        elif index % 2 == 0:
            fileName = bytes.decode(element)

if __name__ == "__main__":
    parser = OptionParser()  
    parser.add_option("--embed", action="store_true", help="Embed files in PDF.")  
    parser.add_option("--extract", action="store_true", help="Extract hidden files.")  
    (options, args) = parser.parse_args() 

    if options.embed and options.extract is None:
        embed(args)
    elif options.embed is None and options.extract:
        extract(args)
