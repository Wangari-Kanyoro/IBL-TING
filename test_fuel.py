from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()


def test_convert ():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    
       

def test_gauge():


    assert convert(50) == "50%"
    assert convert(25) == "25%"
    assert convert(1) == "E"
    assert convert("99/100") == "F"