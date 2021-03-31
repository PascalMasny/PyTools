import time
import math
import decimal
datei = open('4-Digit.txt','w')

#counter
n=0

#counter
for i in range(1,10000):
    print(f"{i:04}")


    datei.write(f"{i:04}")
    datei.write('\n')
    