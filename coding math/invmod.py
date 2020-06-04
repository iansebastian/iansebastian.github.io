def invmod(a, m):
    m0 = m
    x0 = 1
    x1 = 0
    if (m == 1):
        return 0
    
# a = q*m + r
# a_j = a_(j+1)*quot_j + r , a_0 = a, a_1 = m
    while (a > 1):
        q = a // m       # menghitung q_j
        r = a % m

        # Menggeser. indeks a dan m naik. Iterasi pertama, j naik jadi 1.
        a = m               # jadi a_j+1
        m = r               # jadi a_j

        # Update (Menggeser) x0 dan x1
        temp = x1
        x1 = x0 - q*x1
        x0 = temp

        if (x0 < 0):
            x0 += m0
    return x0

print(invmod (175366, 329))
