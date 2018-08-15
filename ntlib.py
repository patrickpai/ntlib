def gcd(a, b):
    """
    Compute gcd(a, b) with the Euclidean Algorithm
    """

    # Normalize input such that a >= b
    if a <= b:
        a, b = b, a

    q_list = []
    r_list = []

    remainder = None

    while remainder != 0:
        quotient = a/b
        remainder = a%b

        q_list.append(quotient)
        r_list.append(remainder)

        a = b
        b = remainder

    # a is a multiple of b
    if len(r_list) < 2:
        return a

    # Return last non-zero remainder
    return r_list[-2]
