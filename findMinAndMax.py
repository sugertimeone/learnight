# _*_ coding: utf-8 _*_
def findMinAndMax(L):
    if L == []:
        return (None, None)
    min = L[0]
    max = L[0]
    for value in L:

        if min > value:
            min = value
        if max < value:
            max = value
    print(L)
    return (min, max)