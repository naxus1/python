import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    cont_d = 0
    cont_valley = 0
    for indice, i in enumerate(s):
        if i == 'D':
            cont_d += 1
        if (i != 'D') or (indice == (len(s) - 1)):
            if cont_d == 3:
                cont_valley += 1 
            cont_d = 0
    return(cont_valley)


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print(result)