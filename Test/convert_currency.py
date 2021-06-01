import forex_python

c = CurrencyRates()
Currency = c.get_rate('USD', 'EUR')  #convert USD to EURO
print(Currency)
