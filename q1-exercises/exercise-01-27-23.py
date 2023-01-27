# Set the variable called first to your first name.

# Set the variable called last to your last name.

# Then set the variable called formatted that interpolates both
# using the .format() method. Make sure you follow this pattern:

first = 'Walter'
last = 'White'
formatted = "First Name: {first}, Last Name: {last}".format(first=first, last=last)
print(formatted)

# Check if choice is 7
from random import randint
choice = randint(1,10)

if choice == 7:
   print("Lucky you!") 
else:
    print("Not so lucky!")
print(choice)

# Assigns a random value as the food choice
from random import choice
food = choice(['apple','grape','bacon','steak','worm','dirt'])

# My code
if (food == 'apple' or food == 'grape'):
    print("fruit")
if (food == 'bacon' or food == 'steak'):
    print("meat")
else:
    print("yuck!")