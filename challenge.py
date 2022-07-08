#!/usr/bin/python3

class Challenge:
    
    def __init__(self, inputFileUrl, outputFileUrl):
        self.inputFileUrl = inputFileUrl if inputFileUrl else "./input.txt"
        self.outputFileUrl = outputFileUrl if outputFileUrl else "./output.txt"
    
    def run(self):
        inputFile = open(self.inputFileUrl,"r")
        outputFile = open(self.outputFileUrl,"w")
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

def main():
    Challenge(None, None).run()

if __name__ == "__main__":
    main()