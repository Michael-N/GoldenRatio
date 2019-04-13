#!./bin/python
'''
Code By Michael Sherif Naguib
Liscence: MIT open source
Date: 2/23/19
@University of Tulsa
Description:  Code to calculate some patterns i was curious about in the golden ratio and the lucas sequence
              it is known that the  phi^n is approx the nth lucas number... round(phi^n) = lucas(n)
              and that the lucas sequence is similar to the fibonacci sequence instead starting at 2
              2 1 3 4 7 11 18 29 .... (Lucas) Fn = Fn-1 + Fn-2
              (The next is the sum of the two previous in the sequence)

              What this program aims to calculate is the difference or gaps that exist between the numbers...

'''

#imports
from decimal import *
getcontext()
import numpy as np
import matplotlib.pyplot as plt
import tqdm
import copy
import random


if __name__ == "__main__":
    #Settings:
    digitPrecision = 100    #the number of phi digits after the decimal point to use... max = 20k (not != calculation precision....)
    goldenRatioFilename = "GOLDEN_RATIO_20k_Places.txt" #the file storing the ratio... credit to https://www.goldennumber.net/phi-million-places/
    numberQuantity = 100   #How many numbers should be generated... (note this will double computationally in the calculation)

    #Read the golden ratio from the file (NOTE the file has newlines) ~~NumberPhile~~
    print("Reading: {0} for {1} digit-precision".format(goldenRatioFilename,digitPrecision))
    GOLDENRATIO = None
    with open(goldenRatioFilename,"r") as numberFile:
        #Read, get rid of newlines, combine, then take the desired digit count
        lines = numberFile.read().splitlines()
        numText = "".join(lines)
        partialDigits = numText[0:2+digitPrecision]
        #assign the Golden Ratio its value
        GOLDENRATIO = Decimal(partialDigits)

    #Calculate the desired quantity
    print("Generating: Lucas Approximates")
    lucasApproximates = []
    for n in tqdm.tqdm(range(0,numberQuantity)):
        lucasApproximates.append(GOLDENRATIO**Decimal(n))

    #generate a duplicate list to round
    print("Generating: Lucas Exacts")
    lucasApproximatesCopy = copy.deepcopy(lucasApproximates)
    lucasNums = list(map(lambda l: l.to_integral_exact(),lucasApproximatesCopy))

    #Calculate the Differences:
    print("Calculating: deltas")
    lucasDeltas=[]
    for i in tqdm.tqdm(range(0,len(lucasNums))):
        lucasDeltas.append(lucasNums[i] - lucasApproximates[i])
    lucasDeltasFloated = list(map(lambda l: float(l),lucasDeltas))
    print(lucasDeltasFloated)
    
    #Format for cordinates
    print("Generating Plot:")
    x_cords = np.array(list(range(0,len(lucasDeltas))))
    y_cords = np.array(lucasDeltasFloated)
    plt.title("Lucas Deltas")
    plt.xlabel("Index")
    plt.ylabel("Deltas (log scale)")
    #plt.xscale("log")
    # Plot the points
    plt.scatter( x_cords,y_cords,c=[(random.random(), random.random(), random.random())], s=np.pi* 3,alpha=0.5)
    plt.show()

