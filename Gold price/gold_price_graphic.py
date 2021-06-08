#Imports
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
import yfinance as yf

#Read Data
Df = yf.download('GC=F', auto_adjust=True)
#keep close colums
Df = Df[['Close']]
#delete missing values
Df = Df.dropna()

# Plot
Df.Close.plot(figsize=(10, 7),color='r')
plt.ylabel("Gold 1oz/$ Price")
plt.title("Gold Price")
plt.show()