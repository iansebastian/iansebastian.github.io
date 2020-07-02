def print_rangoli(size):
    # your code goes here
    key = 96 + size
    row = 2*size - 1
    comp1 = '-'
    comp2 = chr(key)
    len1 = ((4*size - 3) - len(comp2)) // 2
    for i in range(1, 2*size):
        print(comp1*len1 + comp2 + comp1*len1)
        if i == size:
            comp2 = comp2[0:((len(comp2)//2) - 1)] + comp2[(len(comp2)//2 + 3):]
        else:
            if i<size:
                rev = ''.join(reversed(comp2[:2*i-1]))
                comp2 = comp2[:2*i-1] + '-'+ chr(key-i) + '-' + rev
            else:
                comp2 = comp2[0:((len(comp2)//2) - 1)] + comp2[(len(comp2)//2 + 3):]
        len1 = ((4*size - 3) - len(comp2)) // 2
    return None
            

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)    