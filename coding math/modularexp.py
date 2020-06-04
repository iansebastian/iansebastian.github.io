# An Algorithm for Fast Modular Exponentiation
# Something I learned at Num Theory class
# March 7, 2020

def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    c = 1
    while exponent > 0:
        if (exponent % 2 == 1):
            c = (c * base) % modulus
        base = (base * base) % modulus
        exponent = exponent // 2
    return c
x = modular_pow(7651,20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2,10403)
print(x)