vowels = set("aeiouAEIOU")

s = input("Enter any sentence: ")

count = 0

for char in s:
    if char in vowels:
        count += 1

print("Number of vowels in the sentence:", count)
