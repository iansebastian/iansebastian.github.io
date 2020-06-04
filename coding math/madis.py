x = 1000

for i in range (1000):
    if (i%7==0) or (i%10==0) or (i%13==0):
        x=x-1
print(x)