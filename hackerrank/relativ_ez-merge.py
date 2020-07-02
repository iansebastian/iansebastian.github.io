# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    result = []
    for i in range(len(string)//k):
        elem = string[(k*i) : (k*(i+1))]
        prelim_res = ''
        for lett in elem:
            if lett not in prelim_res:
                prelim_res += lett
        result.append(prelim_res)

    for stuff in result:
        print(stuff)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)