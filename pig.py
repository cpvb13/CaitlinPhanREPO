#this actually took me almost two hours because the pigtranslation always printed out funny
 
name = input("Hello, what is your name?")

names = name.split(' ')

namess = list(names)


translation = []
pigtranslation = []
x = 0
for i in namess:
    fix = namess[x]
    space = ' '
    #check for errors
    #print(fix)
    translation.append(str.upper(fix[1]))
    translation.append(str.lower(fix[2:]))
    translation.append(str.lower(fix[0])+'ay ')
    #print("this is the " +str(x) +' '+ str(translation))
    x += 1   
#print("Let's check: "+ str(translation))
#spacing is weird
#prints out like "ig pay atin lay"
#translation.remove(' ')
#translation.replace(' ','')

#print(translation)
pigtranslation = ''.join(translation)
print(pigtranslation)
#print('Oink oink')


