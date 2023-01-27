# Set the variable called first to your first name.

# Set the variable called last to your last name.

# Then set the variable called formatted that interpolates both
# using the .format() method. Make sure you follow this pattern:

first = 'Walter'
last = 'White'
formatted = "First Name: {first}, Last Name: {last}".format(first=first, last=last)
print(formatted)