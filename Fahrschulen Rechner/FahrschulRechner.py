#Reaktionsweg
def reaktionsweg(v):
    return v / 10 * 3
#Bremsweg
def bremsweg(v):
    return (v / 10) * (v / 10)
#Gefarenbremsung
def gefharenbremsung(v):
    return bremsweg(v) / 2
#Anhalteweg
def anhalteweg(v):
    return reaktionsweg(v) + bremsweg(v)


v = int(input("Geschwindigkeit in km/h: "))

print(f"Reaktionsnweg: {reaktionsweg(v)} m")
print(f"Bremsweg: {bremsweg(v)} m")
print(f"Gefahrenbremsung: {gefharenbremsung(v)} m")
print(f"Anhalteweg: {anhalteweg(v)} m")

