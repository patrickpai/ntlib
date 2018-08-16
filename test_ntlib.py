import ntlib

def test_gcd():
    assert ntlib.gcd(24, 52) == 4
    assert ntlib.gcd(9, 27) == 9
    assert ntlib.gcd(14, 35) == 7
    assert ntlib.gcd(15, 28) == 1
    assert ntlib.gcd(123, 456) == 3
    assert ntlib.gcd(119, 259) == 7
    assert ntlib.gcd(259, 119) == 7

def test_rel_prime():
    assert ntlib.rel_prime(14, 15) == True
    assert ntlib.rel_prime(21, 40) == True
    assert ntlib.rel_prime(2, 4) == False

def test_solve_diophantine():
    assert solve_diophantine_helper(10, 25, 105) == 105
    assert solve_diophantine_helper(6, 9, 21) == 21
    assert solve_diophantine_helper(6, 15, 30) == 30
    assert solve_diophantine_helper(10, 20, 100) == 100
    assert solve_diophantine_helper(13, 7, 5) == 5
    assert solve_diophantine_helper(13, 33, 3) == 3
    assert ntlib.solve_diophantine(6, -9, 20) == False
    assert ntlib.solve_diophantine(2, 10, 11) == False
    assert ntlib.solve_diophantine(10, 25, 104) == False
    assert ntlib.solve_diophantine(9, 27, 6) == False

def solve_diophantine_helper(a, b, c):
    '''
    Return LHS with found (x, y)
    '''
    (x, y) = ntlib.solve_diophantine(a, b, c)
    print (x,y)
    return a * x + b * y