#!/usr/bin/python3
import sys

inputFile = open("./input.txt","r")
outputFile = open("./output.txt","w")

try:
    print("analyzing data from './input.file' file...")
    data = inputFile.read().split()
    numbersParam = set(map(int, data[0].split(',')))
    expectedSum = int(data[1])

    expectedNumbers = set( map(lambda x:  expectedSum - x, numbersParam) )
    expectedNumbers.intersection_update(numbersParam)
    numbersFound = sorted(expectedNumbers)

    print("Writing result to './output.txt' file...")
    for value in numbersFound[0:int(len(numbersFound)/2)]:
        outputFile.write('{},{}\n'.format(value, expectedSum - value))

    print("Done")
except IOError:
        print("Unable to create file on disk.")
finally:
    outputFile.close()
    inputFile.close()