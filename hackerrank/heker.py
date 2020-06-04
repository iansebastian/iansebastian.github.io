# Enter your code here. Read input from STDIN. Print output to STDOUT
turn = list(map(int, input().rstrip().split()))
due = list(map(int, input().rstrip().split()))

if turn[2] > due[2]:
    fine = 10000
else:
    if turn[2] == due[2]:
        if turn[1] > due[1]:
            fine = 500*(turn[1]-due[1])
        else:
            if turn[1] == due[1]:
                if turn[0] > due[0]:
                    fine = 15*(turn[0]-due[0])
                else:
                    fine = 0
            else:
                fine = 0
    else:
        fine = 0
print(fine)