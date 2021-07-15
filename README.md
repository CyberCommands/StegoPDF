Steganography PDF
=================
[![Python3.x](https://img.shields.io/badge/python-3.x-FADA5E.svg?logo=python)](https://www.python.org/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-red.svg)](https://www.python.org/dev/peps/pep-0008/)

Embed/Hide anything inside any PDF files

The script appends files as raw bytes at the end of any PDF. Your files will be not really "hidden".

PDF-Readers ignore these parts and don't "see" them.

## Usage:
```
$ python3 stego.py -h
Usage: stego.py [options]

Options:
  -h, --help  show this help message and exit
  --embed     hide files in PDF
  --extract   extract hidden files
```

Embed:
```
$ python3 stego.py --embed <PDF file> <File to hide>
$ python3 stego.py --embed example.pdf example.txt
```

Extract:
```
$ python3 stego.py --extract <PDF file>
$ python3 stego.py --extract example.pdf
```
