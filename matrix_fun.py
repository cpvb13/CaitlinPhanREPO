#matrix_fun.py 00:36 6.13.18
import numpy as np
n = []

x = 1
while x <= 4:
    ask = input("What is your lucky #"+str(x)+"?")
    x += 1
    n.append(int(ask))
    #check print(ask)


a = n[0]
b = n[1]
c = n[2]
d = n[3]
denominator = a*d - b*c
if denominator == 0:
    print('The invertibility of this matrix is not availible!')
else:
    constant = float(denominator)**-1.0
    z = float(constant)
   
    #print(constant)
    #ac
    matrix = np.array([a,b,c,d])
    rows = matrix.ndim
    columns = matrix.shape
    numbers = matrix.size

    e=d*z
    f=-b*z
    g=-c*z
    h=a*z
    
    inverse = [e,f,g,h]

    print(inverse)

    print(f'This is your matrix:(({a},{b}), ({c},{d}))')
    print(f'This is your inverse matrix:(({e},{f}), ({g},{h}))')

