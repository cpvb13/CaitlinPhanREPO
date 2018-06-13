price_str = input("Enter the price of a meal: ")
price = float(price_str)

tip = price * 0.16
total = price + tip

print("\nA 16% tip would be", tip)
print("The total including the tip would be", total)
print('Bon Appétit')