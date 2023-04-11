#!/usr/bin/python3
""" This scripts read each line from the stdin and calculates the meterics """

import sys

def printstatistics(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))

statistics_array = {
    "200": 0, 
    "301": 0, 
    "400": 0, 
    "401": 0, 
    "403": 0,
    "404": 0, 
    "405": 0, 
    "500": 0
}

count = 0
size = 0

try:
    for ln in sys.stdin:
        if count != 0 and count % 10 == 0:
            printstatistics(statistics_array, size)
        statlist = ln.split()
        count += 1
        try:
            size += int(statlist[-1])
        except:
            pass
        try:
            if statlist[-2] in statistics_array:
                statistics_array[statlist[-2]] += 1
        except:
            pass
    printstatistics(statistics_array, size)
except KeyboardInterrupt:
    printstatistics(statistics_array, size)
    raise