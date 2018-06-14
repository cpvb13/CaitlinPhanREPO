#Palindrome 


inpu = input("Enter your name: ")
#inpu = 'John'
#inpu = "Caitlin Phan"
#name = list(name)

name = inpu.split(' ')
words = len(name)
#2
palindrome = []


j=0
while j<words:
    palindrome.append(name[j][::-1])
    j+=1
    
name_b = ' '.join(palindrome)
name_b = name_b.title()
print("Olleh "+name_b+'!')

if name_b == inpu:
    result ='a palindrome!'
else:
    result ="not a palindrome :("

print('Your name is '+result)

