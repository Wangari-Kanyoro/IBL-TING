from numb3rs import validate



def main():
    test_ip_ture()
    test_ip_false()




def test_ip_ture():
    assert validate("456.456.456.456") == True
    assert validate("45.46.4.456") == True


def test_ip_false():
    assert validate("4566.456.456.456") == False
    assert validate ("1.444.444.444") == False
    assert validate("dog") == False


if __name__ == "__main__":
    main()
