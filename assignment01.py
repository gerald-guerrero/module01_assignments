name = input("Enter your name: ") # the input() function will prompt the user for their name
print("Hello, " + name + "! Nice to meet you.")
length_of_name = len(name) # Length of the user input will be stored in the variable
print("Your name has " + str(length_of_name) + " characters.") # Prints the number of characters in the user input
print("In uppercase, your name looks like: " + name.upper()) # Prints the user input in all upper-case letters using the .upper() string function