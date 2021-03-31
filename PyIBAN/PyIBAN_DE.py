#IBAN abfrage
iban = input("IBAN: DE")

#
laendercode = iban[:2]
pruefziffer = iban[2:4]
blz = iban[4:12]
konntonr = iban[12:].zfill(10)

check = str(98 - int(blz + konntonr + "131400") %97).zfill(2)

if check == pruefziffer:
    print("Die IBAN ist korekt!")
else:
    print("Die IBAN ist falsch!")


