"""
ntlib - Python library for performing common operations in Number Theory
"""

def gcd(a, b):
    """
    Compute and return gcd(a, b)
    """

    # Normalize input such that a >= b
    if a <= b:
        a, b = b, a

    return _perform_euclidean_algo(a, b)[0]

def _perform_euclidean_algo(a, b):
    '''
    Return list of quotients and list of remainders found with the Euclidean Algorithm
    '''

    b_original = b

    q_list = []
    r_list = []

    remainder = None

    while remainder != 0:
        quotient = a / b
        remainder = a % b

        q_list.append(quotient)
        r_list.append(remainder)

        a = b
        b = remainder

    # Let gcd(a, b) = d
    gcd_a_b = None

    # one of a, b is a multiple of the other
    if len(r_list) == 1:
        gcd_a_b = b_original
    # Return last non-zero remainder
    else:
        gcd_a_b = r_list[-2]

    return (gcd_a_b, q_list, r_list)

def rel_prime(a, b):
    """
    Return True if a and b are relatively prime/mutually prime/coprime
    """

    return gcd(a, b) == 1

def solve_diophantine(a, b, c):
    """
    Return (x, y) such that ax + by = c or False if no solutions exist
    """

    swapped = False

    # Normalize input such that a >= b
    if a <= b:
        swapped = True
        a, b = b, a

    (gcd_a_b, quotients, remainders) = _perform_euclidean_algo(a, b)

    # Equation has a solution
    if c % gcd_a_b == 0:
        index = len(quotients) - 2

        # Right hand side of equation gcd = rhs
        rhs = {}

        while index >= 2:
            quotient = quotients[index]
            remainder = remainders[index]
            prev_remainder = remainders[index - 1]
            second_prev_remainder = remainders[index - 2]

            if len(rhs) == 0:
                rhs[second_prev_remainder] = 1
                rhs[prev_remainder] = -1 * quotient
            else:
                rhs[prev_remainder] += -1 * quotient * rhs[remainder]
                rhs[second_prev_remainder] = rhs[remainder]
                del rhs[remainder]

            index -= 1

        quotients_len = len(quotients)

        # a is a multiple of b
        if quotients_len == 1:
            rhs[a] = 0
            rhs[b] = 1
        elif quotients_len == 2:
            rhs[a] = 1
            rhs[b] = -1 * quotients[0]
        elif quotients_len == 3:
            rhs[b] = 1
            rhs[remainders[0]] = -1 * quotients[1]

            rhs[a] = rhs[remainders[0]]
            rhs[b] += -1 * quotients[0] * rhs[remainders[0]]
            del rhs[remainders[0]]
        else:
            # Equation of the form b = q2r1 + r2
            rhs[b] = rhs[remainders[1]]
            rhs[remainders[0]] += -1 * quotients[1] * rhs[remainders[1]]
            del rhs[remainders[1]]

            # Equation of the form a = q1b + r1
            rhs[a] = rhs[remainders[0]]
            rhs[b] += -1 * quotients[0] * rhs[remainders[0]]
            del rhs[remainders[0]]

        # Scale whole equation to match desired c
        scale_factor = c / gcd_a_b
        rhs[a] *= scale_factor
        rhs[b] *= scale_factor

        return (rhs[b], rhs[a]) if swapped else (rhs[a], rhs[b])
    # Equation has no solutions
    else:
        return False

