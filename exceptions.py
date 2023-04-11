
try:
    x=int(input("Enter the value of x?"))
    print(f" x is {x}")

except ValueError:
   print ("Invalid input")

try: 
   x=int(input("Enter the value of x?"))
   print(f" x is {x}")
except ValueError:
   print ("Invalid input")
else:
   print ("x is valid")
   

   


