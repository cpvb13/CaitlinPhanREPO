
#num = int(input('Pick a number, more than one: '))
n = int(input("Enter a number: "))

fn = [1,1]
x = 1

while n >= int(fn[x]):
    fn.append(int(fn[x-1])+int(fn[x]))
    x += 1

#print(fn) --- last in list was greater than input number 
for i in fn:
    if n < fn[-1]:
        fn.remove(fn[-1])

fn = str(fn).strip('[]')
print(fn)


#new =' '.join(fn)
#--- still printed a list of strings
#print(new)
