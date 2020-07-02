# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

elm1 = '-'
elm2 = '.|.'
elmC = 'WELCOME'

a, b = map(int, sys.stdin.readline().split())

for i in range(a//2):
    n1 = (b - 3*(2*i+1))//2
    print(elm1*n1 + elm2*(2*i+1) + elm1*n1)

print(elm1*((b-7)//2) + elmC + elm1*((b-7)//2))

for i in range(a//2 - 1,-1,-1):
    n1 = (b - 3*(2*i+1))//2
    print(elm1*n1 + elm2*(2*i+1) + elm1*n1)
