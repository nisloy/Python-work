input_string=input('Input anny string you want: ')
vowels = set("aeiouAEIOU")
found_vowels=[]
for char in input_string:
    if char not  in vowels and char not in found_vowels:
        found_vowels.append(char)
print(f"Vowels found in the string: {''.join(found_vowels)}")


# def find_upper_case(input_string):
#     capitals=[]
#     for char in input_string:
#         if char.isupper():
#             capitals.append(char)
#     return capitals

# word=input("Enter any string: ")
# capital_letters=find_upper_case(word)

# if word:
#  print(f"Found capitalks{''.join(word)}")