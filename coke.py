amount_due = 50
coins_added = 0

while True:
    insert_coin = int(input("Insert coins: "))
    if insert_coin == 25 or insert_coin == 10 or insert_coin ==5:
       amount_due -= insert_coin
       coins_added += insert_coin

    if coins_added >= 50:
        print(f"change to be returned: {coins_added - 50}")
    
        break




