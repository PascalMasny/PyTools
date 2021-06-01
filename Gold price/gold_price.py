#Import
from yahoo_fin import stock_info

# get 1oz gold price
gold_oz_dollar = stock_info.get_live_price("GC=F")
# 1oz$ to 1g$
gold_1g_dollar = gold_oz_dollar / 28.34952
# 1g$ to 1g€
gold_1g_euro = gold_1g_dollar * 0.7618

#inptuz
g = input ("mass in gramm (1 - 1000): ")

#Print
print("1oz Gold price: " , gold_oz_dollar , "$")
print("1g Gold price: " , gold_1g_dollar , "$")
print("1g Gold price: " , gold_1g_euro , "€")
print("")

"""   !!!!int BIG!!!!!
print(g, "g Gold price: " + g* gold_1g_dollar, "$")
print(g, "g Gold price: " + g* gold_1g_euro, "€")
"""
