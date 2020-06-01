import time

def GenerateTitle():
    print("==============================================")
    print("        LINEAR CONGRUENCE SYSTEM SOLVER   ")
    print("an implementation of Chinese Remainder Theorem")
    print("==============================================")

def invmod(a, m):
    # Tujuan fungsi ini adalah untuk memperoleh nilai x dari masalah kongruensi ax = 1 (mod m).
    # Metode yang digunakan untuk melakukan hal tersebut adalah Extended Euclid Algorithm.
    # Keluaran yang dihasilkan adalah nilai x.


    # Inisialisasi variabel:
    # m0 : nilai m awal. Disimpan untuk dipakai nanti 
    # x0 dan x1 : menyimpan x_j dan x_(j+1)
    m0 = m
    x0 = 1
    x1 = 0

    # Kasus m = 1 adalah kasus spesial, sebab langsung bisa diperoleh hasil x = 0.
    if (m == 1):            
        return 0    
# a = q*m + r
# a_j = a_(j+1)*quot_j + r , a_0 = a, a_1 = m

    # Ini adalah bagian utama pelaksanaan algoritma Euclid.
    # Bentuk persamaannya adalah : a = q*m + r, dengan keterangan sbb:
    # a, m : nilai input;
    # q : quotient;
    # r : remainder.
    
    while (a > 1):
        # Menghitung nilai q dan r pada iterasi ke-j,
        q = a // m       
        r = a % m

        # a dan m kini hanya berfungsi untuk menentukan nilai q dan r. 
        # Oleh sebab itu, a dan m langsung dipersiapkan untuk iterasi berikutnya,
        # dengan "menggeser" nilainya, seperti perlanjutan langkah pada algoritma Euclid.
        # Alhasil, a dan m kini memiliki nilai untuk iterasi ke - (j+1).
        a = m              
        m = r              

        # Pada langkah ini, nilai x_j dan x_j+1 di-update. 
        temp = x1
        x1 = x0 - q*x1      # jadi x_j+1
        x0 = temp           # jadi x_j

        if (x0 < 0):        # jika x_j negatif, maka dijumlah m0, shd jd positif
            x0 += m0

    # Yang kita cari adalah nilai x_j. Oleh sebab itu, keluaran yang diberikan adalah variabel x0.        
    return x0

#################
# LANGKAH UTAMA #
#################

GenerateTitle()
# Kode untuk menerima input berupa jumlah persamaan dalam sistem, serta 
# nilai a_i dan m_i untuk setiap persamaan dalam sistem, yang berbentuk
# x = a_i (mod m_i).

n = int(input("Masukkan banyak sistem: "))
a =[None for i in range(n)]                     #Array untuk menyimpan a
m =[None for i in range(n)]                     #Array untuk menyimpan residue m
D =[None for i in range(n)]                     #Array untuk menyimpan hasil bagi M/m, di mana M = m1*m2..*mn
c =[None for i in range(n)]                     #Array untuk sisa bagi D dengan m

dummy = [0 for i in range(n)]
M=1
num = 0

for i in range (n):
    a[i] = int(input("Masukkan a" + str(i + 1) + ": "))
    m[i] = int(input("Masukkan residue m" + str(i + 1) + ": "))

start_time = time.time()
for i in range (n):
    M = M*m[i]

# Lalu, dihitung juga  M/m[i], serta residu M/m[i] modulo m[i], sebagai cara untuk
# memperkecil angka yang digunakan dalam perhitungan nantinya.

for i in range (n):
    D[i] = M//m[i]
    c[i] = D[i] % m[i]

# Sampai langkah ini, maka yang harus diselesaikan adalah linear congruence berbentuk
# c_i * y_i = a_i (mod m_i).
# Persamaan tersebut dapat diselesaikan dengan mudah dengan menggunakan inverse modulo.
# Setelah iterasi terakhir, akan diperoleh 
f = 0

for i in range (n):    
    f += invmod(c[i],m[i]) * a[i] * D[i]

f = f % M

print("\nNilai x adalah {} modulo {}.".format(f, M))

print("\nTime Elapsed : {}".format(time.time()-start_time))