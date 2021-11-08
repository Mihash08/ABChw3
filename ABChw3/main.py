import sys
import string
from random import randrange

from extender import *

#----------------------------------------------
if __name__ == '__main__':
    if len(sys.argv) == 4:
        if sys.argv[1] == "-f":
            inputFileName  = sys.argv[2]
            outputFileName = sys.argv[3]
            file = True
        else:
            randomFiguresCount = int(sys.argv[2])
            outputFileName = sys.argv[3]
            file = False
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f":
            inputFileName  = sys.argv[2]
            file = True
        else:
            randomFiguresCount = int(sys.argv[2])
            file = False
        outputFileName = "output.txt"
    else:
        print("Incorrect command line! You must write: python main -f <inputFileName> [<outputFileName>]"
              "\nor -r <randomFiguresCount> [<outputFileName>]")
        exit()
    line = ""
    if file:
        ifile = open(inputFileName)
        line = ifile.read()
        ifile.close()
    else:
        for i in range(0, randomFiguresCount):
            figType = randrange(3) + 1
            if figType == 1:
                line += str(figType) + " " + str(randrange(20) + 1) + " " + str(randrange(20) + 1) + " "
            elif figType == 2:
                line += str(figType) + " " + str(randrange(20) + 1) + " " + str(randrange(20) + 1) + " "\
                        + str(randrange(20) + 1) + " " + str(randrange(20) + 1) + " "
            elif figType == 3:
                line += str(figType) + " " + str(randrange(20) + 1) + " " + str(randrange(20) + 1) + " "
    strArray = line.replace("\n", " ").split(" ")
    strArray = list(filter(None, strArray))
    print('==> Start')

    container = Container()
    figNum = ReadStrArray(container, strArray)
    container.Print()

    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    container.ShellSort()
    print("\nSorted container:\n")
    container.Print()
    ofile.write("\nSorted container:\n\n")
    container.Write(ofile)
    ofile.close()


    print('==> Finish')
