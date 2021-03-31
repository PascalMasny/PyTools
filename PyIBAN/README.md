# PyIBAN
Ein Pythn IBAN Checker für Deutsche IBANs. Achtung!: überprüft NUR dir Richtigkeit nach der IBAN-Prüfsumme, nicht die existenz der IBAN.  

# IABN Algorithmus:
98 - (Banklaeitzahl + Kontonummer + Ländercode-DE-131400) mudolo 97 + 00 == Prüfziffer der IBAN 
