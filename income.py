
income = int(input("Please enter your income:"))
tax = 0
if income <= 1000:
    tax += 0.05*income

if income > 1000:
    tax += 0.05*1000
    if income <= 2000:
        tax += 0.10*(income-1000)

if income > 2000:
    tax =+ 0.05*1000
    tax =+ 0.10*1000
    tax =+ 0.15*(income-2000)
#tax=int(tax)
#print("You will pay $"+str(tax)+".00 !")


tax = float(tax)
ntax = round(tax,2)
print("You will pay:")
print(float(tax))

#print("You will pay $"+str(tax)+" !")
#TypeError: must be str, not float... butt still missing last deci
