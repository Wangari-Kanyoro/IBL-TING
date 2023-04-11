name = input("Enter: ")
print("output:")

for letter in name:
    
    if not letter in ['a', 'e', 'i', 'o', 'u']:
        print(letter)

print()
