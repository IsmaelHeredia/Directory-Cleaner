#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Directory cleaner 0.3
# Written By Ismael Heredia in the year 2020

import argparse
import os

from modules import directoryCleaner

def main():
    parser = argparse.ArgumentParser(description="Enter arguments to use the script")	
    parser.add_argument("-clean", dest="clean", help="Enter directory to clean")
    parser.add_argument("-clean-downloads", action="store_true", help="Clean downloads directory")

    results = parser.parse_args()

    clean = results.clean
    clean_downloads = results.clean_downloads

    if clean != None:
        dirclean = directoryCleaner.directoryCleaner()
        dirclean.clean_directory(clean)
    elif clean_downloads == True:
        dirclean = directoryCleaner.directoryCleaner()
        dirclean.clean_directory(os.path.join(os.path.expanduser("~"), "Downloads"))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()