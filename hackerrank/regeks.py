import re
""" https://www.w3schools.com/python/python_regex.asp """

if __name__ == '__main__':
    N = int(input())
    names = []
    gmail = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        names.append(firstName)
        x = re.search(r"@gmail\.com$", emailID)
        if x:
            gmail.append(N_itr)
    result = [names[i] for i in gmail]
    result.sort()
    for name in result:
        print(name)
