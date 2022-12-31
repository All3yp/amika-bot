#!/bin/python3

from selenium import webdriver
import time
import sys

import src

# Main
if __name__ == '__main__':
    n = int(sys.argv[1])
    src.generateName(n)
    src.generateEmail(n)