# Easy
sentence = input("What do you want to say? ")   # Input the Statement
input_string = sentence.lower()  # Make it all LC
vowel_count = sum(1 for char in sentence if char in 'aeiou')  # Check Each Character for aeiou and Sum the Instances
print(vowel_count)