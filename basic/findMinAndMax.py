# _*_ coding: utf-8 _*_
def findMinAndMax(L):
    if not isinstance(L,Iterable):
        print('Type Error!')
        return L

    min = max = None

    #拦截空list
    if len(L) == 0:
        return (min,max)
    #非空操作
    min = max = L[0]
    for i in L:
        if i <= min:
            min = i
        elif i >= max:
            max = i
    return (min,max)
