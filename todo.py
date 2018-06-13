'''Your program should have the following elements:

Empty dictionary to store information

Key for each day of the week

Each key has a list value that stores items

User is prompted to add to or view to-do list

User can type "add" program will ask what day and add it correctly

User can type "get" and the program will ask for the day and print the values

User can type "quit" to exit the loop
'''
a = 'You have to'
to_do = {"You have to ": 'Monday','You have to ': 'Tuesday','You have to ': 'Wednesday','You have to ': 'Thursday','You have to ': 'Friday','You have to ': 'Saturday','You have to ': 'Sunday'}
#day = key when calling to_do[key]
print(to_do[1])

input1 = input("What would you like to do?")
if input1 == 'add':
    input2 =input('What day?')
    day = input2
    input3 = input("What would you like to add to " +day +"'s to-do list?")    
else:
    print("Sorry, I cannot do that.")
#to_do

