#第一种方法
'''
def romanToInt1(s):
    result = 0
    curr = 0
    pre = 0
    for i in range(len(s)):
        if s[i] == 'I':
            curr = 1
        elif s[i] == 'V':
            curr = 5
        elif s[i] == 'X':
            curr = 10
        elif s[i] == 'L':
            curr = 50
        elif s[i] == 'C':
            curr = 100
        elif s[i] == 'D':
            curr = 500
        elif s[i] == 'M':
            curr = 1000

        result = result + curr

        if (pre < curr):
            result = result - 2 * pre
        pre = curr

    return result
'''
#第二种方法
def romanToInt1(s):
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0

    for i in range(len(s)-1):
        if d[s[i]] < d[s[i+1]]:
            result-= d[s[i]]
        else:
            result+=d[s[i]]

    result+=d[s[len(s)-1]]
    return result

