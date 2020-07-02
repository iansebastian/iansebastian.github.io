# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    ref_vowels = ['A', 'E', 'I', 'O', 'U']
    idx_conso = []
    idx_vowel = []
    scoreA = scoreB = 0

    for i in range(len(string)):
        if (string[i] in ref_vowels):
            idx_vowel.append(i)
        else:
            idx_conso.append(i)

    scoreA = sum(list(len(string) - k for k in idx_conso))
    scoreB = sum(list(len(string) - k for k in idx_vowel))

    if scoreA > scoreB:
        print('Stuart', scoreA)
    elif scoreB > scoreA:
        print('Kevin', scoreB)
    else:
        print('Draw')
 
if __name__ == '__main__':
    s = input()
    minion_game(s)