import math

rate = input("Please type the current exchange rate ")
amount = input("Please put in the amount of currency to convert ")
rate = float(rate)
amount = float(amount)

total = rate * amount
result = total - 3.00

print(result)

