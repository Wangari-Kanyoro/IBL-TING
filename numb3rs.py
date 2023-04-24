import re



def main():
    print(validate(input("IPV4 Address:")))


def validate(ip):
    valid = re.search(r"^[0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
    if valid:
        for i in range(1, 5):
            if int(valid.group(i)) > 225:
                return False
            return True
        else:
            return False







if __name__ == "__main__":
    main()
