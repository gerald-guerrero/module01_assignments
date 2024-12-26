n = 0
while(n <= 0): # The loop will continue to ask the user for a positive integer if the user does not provide one
    n = int(input("Enter a positive integer: "))

total = 0
for i in range(1, n+1): # The loop iterates through all integers from 1 to the user's input integer and adds it to the total
    total += i

print("The sum of numbers from 1 to " + str(n) + " is " + str(total)) # The print statement shows the computed total based on the user's input