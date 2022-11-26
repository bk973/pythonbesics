#This program prompts the user to input their age
#Prints the age to the standard output
#Adds 1 year to age and prints the result to the standard output

#Note::
#The input value is always received as text 
#We use a special function int() inorder to turn it into an integer...
age = input('How old are you? \n');

nextAge = int(age) + 1

print(f"You're {age} years old this year")
print(f"Next year you'll be {nextAge} years old")