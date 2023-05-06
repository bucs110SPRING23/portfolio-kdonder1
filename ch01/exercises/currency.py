import math

rate = input("Please type the current exchange rate ")
amount = input("Please put in the amount of currency to convert ")
rate = float(rate)
# float allows the variable to have a decimal
# in this code, the variable is 'cast' to be a float
amount = float(amount)

total = rate * amount
result = total - 3.00
# when you subtract a float from an int., the result will always be a float

print(f"You're result minus a small convenience fee is ${result:.2f}")

