def main():
    answer = input("pleasantries: ")
    print(value(answer))




def value(answer):
    answer= answer.lower().strip()

    if answer[:5] == "hello":
      return "$0"


    elif answer[0] == "h":
     return "$20"

    else:
     return "$100"
          

if __name__ == "__main__":
    main()