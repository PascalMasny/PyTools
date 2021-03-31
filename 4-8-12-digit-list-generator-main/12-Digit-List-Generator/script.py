import time
import math
import decimal
datei = open('12-Digit.txt','w')

#counter
n=0

#counter
for i in range(1,1000000000000):
    print(f"{i:012}")


    datei.write(f"{i:012}")
    datei.write('\n')
    