camelCase= input("What is your name:")
snake_case = ""

for i in range(len(camelCase)):


    if camelCase.isupper():
        snake_case = snake_case + '_' + camelCase[i]. lower()
    else:
        snake_case += camelCase[i]

    print("snake_case:" , snake_case)


    