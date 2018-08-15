import ntlib

def test_gcd():
    assert ntlib.gcd(24, 52) == 4
    assert ntlib.gcd(9, 27) == 9
    assert ntlib.gcd(14, 35) == 7
    assert ntlib.gcd(15, 28) == 1
    assert ntlib.gcd(123, 456) == 3
    assert ntlib.gcd(119, 259) == 7

    assert ntlib.gcd(259, 119) == 7
