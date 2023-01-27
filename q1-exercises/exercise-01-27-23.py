# Exercise 6: Lesson 56 - Formatted Strings

# Set the variable called first to your first name.
# Set the variable called last to your last name.
# Then set the variable called formatted that interpolates both
# using the .format() method. Make sure you follow this pattern:

first = 'Walter'
last = 'White'
formatted = "First Name: {}, Last Name: {}".format(first, last)
print(formatted)

# Check if choice is 7
from random import randint
choice = randint(1,10)



# Exercise 7: Lesson 63 - Lucky Number
if choice == 7:
   print("Lucky you!") 
else:
    print("Not so lucky!")
print(choice)


# Exercise 9: Lesson 69 - Food Classifying
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




# Exercise 10: Lesson 73 - Positive or Negative?
# Checks if value is positive or negative

from random import randint
x = randint(-100,100)
while x == 0:
    x = randint(-100,100)

y = randint(-100,100)
while y == 0:
    y = randint(-100,100)

# My code
if(x > 0 and y > 0):
    print("both positive")
if(x < 0 and y < 0):
    print("both negative")
if(x > 0 and y < 0):
    print("x is positive and y is negative")
if(x < 0 and y > 0):
    print("x is negative and y is positive")