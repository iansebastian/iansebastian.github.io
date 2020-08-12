def decimal_len(x):
    """Counts the length of a decimal number, i.e. the greatest power of 10 smaller than x."""
    r = 1
    while x >= 10:
        x /= 10
        r += 1
    return r


def decimal_sqrt(p, depth=0):
    """
    Performs a digit-by-digit decimal estimate of the square root of p, down to a specifyied digits behind decimal point.
    :param p: float
        A decimal number whose square root is being estimated.

    :param depth: int
        Number of floating points to calculate.

    :return: float
        Square root estimate of p.
    """
    dlen = decimal_len(p)
    res = 0

    for i in range ((dlen-1) // 2, -depth-1, -1):
        pos = p / 100**i

        r = 20 * res
        s = 0
        while ((r+s) * s) <= pos:
            s += 1
        s -= 1

        res = 10*res + s
        p -= (r+s)*s * 100**i
        print(pos, p, res, r, s)
    return res / 10**depth
