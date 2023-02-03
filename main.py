#!/usr/bin/python3
import requests
import sys
import argparse
import re
import string
from getUrl import main as getUrl

parser = argparse.ArgumentParser('claster: get all url in website')
parser.add_argument('-f','--file' , help='get File')
parser.add_argument('-a','--all', help='use all function')
parser.add_argument('-u','--url',type=str,help="url for website")
args = parser.parse_args()

class MainClass:
    def mian_getUrl(url):
         getUrl(url)





def main():
    main_class = MainClass()
    url = args.url
    allFunctions = args.all
    allFile = args.file
    MainClass.mian_getUrl(url)

    return 0

if __name__ == "__main__":
    main()        
