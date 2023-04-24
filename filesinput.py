name = input("Whats your name")

#file = open("names.txt", "a")
#file.write("(names),\n")
#file.close()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
    
