#Input
import string

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)

def rot13(msg):
    result = ""
    
    for character in msg:
        if character in upper:
            result += upper[(upper.index(character) + 23) % 26]
        elif character in lower:
            result += lower[(lower.index(character) + 23) % 26]
        else:
            result += character
        
    return result

#Input
print(rot13("Hello World"))