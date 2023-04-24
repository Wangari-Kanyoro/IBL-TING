from datetime import date
import inflect
import sys


p = inflect.engine ()



def main():
    try:
        year, month, day = input("Date of birth").split(".")
    except ValueError:
        sys.exit("Date is invalid")

    minutes_lived(year,month, day)

def minutes_lived(year, month, day):
    try:

      dt = date( int(year), int(month), int(day))
    except ValueError:
        return "Date is invalid"
    tday = date.today()
    diff = tday - dt 

    minutes = int(diff.ttotal_seconds()/ 60)
    msg = p.number_to_words(minutes , andword="") + "minutes"
    return msg.capitalize()




if __name__ == "_main_":
    main()