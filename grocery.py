grocery = {}

while True:
    try:
     name = input("enter ")
    except EOFError:
       print ()
       break
    if name. upper() in grocery:
       grocery[name.upper()] +=1
    else: 
       grocery[name.upper()] = 1

       
       print (grocery[name], )

