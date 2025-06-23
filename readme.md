# Amount Extractor

A sleek, terminal-based amount extractor, used to extract and evaluate monetary figures

![Python](https://img.shields.io/badge/python-3.10+-green.svg)


## Table of Contents
- [About](#about)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [License](#license)

## About
AMOUNT EXTRACTOR as the name suggest its a tool that extracts monetary figures from a pool of text and perform mathematical operations on them to get you answer. This saves you time in manual picking the figure and adding it.

## Features
- Fast
- Sumation
- Product
- Average

## Demo
```bash 
# Interactive
$ python amount_extractor.py --operation average --currency ₦ --banner

# From a file
$ python amount_extractor.py --file transactions.txt --operation sum --export summary.txt

# Pipe data
$ echo "I paid ₦5000, $200, and ₦1500.50" | python amount_extractor.py --currency ₦

``` 

## Installation
```bash
$ git clone https://github.com/Crypt-atu/Amount_Extractor.git
$ cd AMOUNT_EXTRACTOR
$ pip install -r requirements.txt
```


## License
XiCrypt©[crypt_atu]
