def print_formatted(number):
    # your code goes here
    b_mxlen = len(bin(number)) - 1

    for i in range (1, number+1):
        b_i = bin(i)[2:]
        o_i = oct(i)[2:]
        h_i = hex(i)[2:].upper()
        print(str(i).rjust(b_mxlen-1) + o_i.rjust(b_mxlen) + h_i.rjust(b_mxlen) + b_i.rjust(b_mxlen))

    pass
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)