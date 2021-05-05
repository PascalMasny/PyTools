# https://www.youtube.com/watch?v=De4bBinTaxQ
#Imports
import secrets

pw = ""

char = "QWERTZUIOPÜASDFGHJKLÖÄYXCVBNMqwertzuiopüasdfghjklöäyxcvbnm1234567890"
length = int(input("Password length: "))

for _ in range(length):
    pw = pw + secrets.choice(char)

print(pw)