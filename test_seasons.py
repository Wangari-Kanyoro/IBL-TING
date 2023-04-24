from seasons import minutes_lived


def main():
    test_1()
    test_2()

def test_1( ):
    assert minutes_lived( 2003, 5, 17) == "Ten million, four hundred and eighty three thousand, two hundred minutes"
    assert minutes_lived(2002, 4, 23 ) == "Eleven million, forty three thousand, three hundred and sixty minutes"

def test_2():
    assert minutes_lived()


if __name__ == "__main__":
    main()