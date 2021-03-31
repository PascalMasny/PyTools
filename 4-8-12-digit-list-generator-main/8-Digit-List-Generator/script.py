import time
import math
import decimal
datei = open('8-Digit.txt','w')

#counter
n=0

#counter
for i in range(1,100000000):
    print(f"{i:08}")


    datei.write(f"{i:08}")
    datei.write('\n')
    