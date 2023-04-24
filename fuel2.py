
def main():
  
  num= input("Fraction: ")
  percentage = convert(num)
  print(gauge(percentage))

def convert(num):

 while True:
    num= input("Fraction: ")
    index = num.find("/")
    try:
        x= int(num[:index])
        y= int(num[index+1:])
        fraction = x / y
        if x> y:
            num = input("Fraction:  ")
            continue
        else:
           percentage = int(fraction * 100)
           return percentage
    except (ValueError, ZeroDivisionError):
        continue
    

def gauge(percentage):


  if percentage> 99:
    print("F")
  elif percentage < 1:
    print("E")
  else:

    return(str(percentage) + "%")
  

  if __name__ == "__main__":
     main()

