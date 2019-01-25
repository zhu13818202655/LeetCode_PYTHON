''' Given a 32-bit signed integer, reverse digits of an integer.'''
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == -2 ** 31:
        return 0
    reversestr = ''
    if x < 0:
        reversestr = '-'
    x = abs(x)
    string = str(x)
    for i in range(len(string) - 1, -1, -1):
        if i == len(string) - 1 and string[i] == 0:
            continue
        reversestr += string[i]
    x = int(reversestr)
    if x < -2 ** 31 or x > 2 ** 31 - 1:
        return 0
    else:
        return x
