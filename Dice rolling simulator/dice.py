#Imports
import random

repeat = True

while repeat:
    print("You rolled" , random.randint(1,6)) #random betwen 1 and 6
    print("Dou you want to roll again? Y/N") #ask
    repeat = ("y" or "yes") in input().lower() #ask => input lower => repeat/exit