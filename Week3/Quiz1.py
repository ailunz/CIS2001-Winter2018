# Write a script that prompts the user for the temperature
# if the temperature is greater than 32, display "It is raining"
# if the temperature is not greater than 32, display "It is snowing"
# Question 1

temp = int( input("Please enter the temperature") )

if temp >= 32:
    print("It is raining")
else:
    print("It is snowing")

# Given the list
# groceries = [ 'Apples', 'Bananas', 'Bread', 'Milk' ]
# write a script that loops through the list printing every item
# Question 2

groceries = [ 'Apples', 'Bananas', 'Bread', 'Milk' ]

# using this for loop I can't change the original list
for item in groceries:
    print(item)

# this is used if I need to change the values in the list
for index in range( len(groceries) ):
    print(index+1, ':', groceries[index])