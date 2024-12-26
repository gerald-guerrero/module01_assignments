sentence = input("Enter a sentence: ") # The input() function prompts the user for a sentence 
sentence = sentence.lower() # the sentence is converted to all lower case letters for consistency
vowel_count = 0
for char in sentence: # The loop iterates through characters in the sentence 
    if char in "aeiou": # The if statement checks if the current character matches any in the standard list of vowels and increments the vowel count if true
        vowel_count += 1

print("The total number of vowels in your sentence is:", vowel_count) # Prints the computed total of vowels found in the user input