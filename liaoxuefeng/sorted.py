#1.
print(sorted([36, 5, -12, 9, -21]))

#2.
print(sorted([36, 5, -12, 9, -21], key=abs))

#3.
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

#4.
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

#5.
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

#6.
L = [('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
#按名字排序
def by_name(t):
    return t[0]
L2 = sorted(L,key=by_name)
print(L2)

#按成绩排序
def by_score(t):
    return t[1]
L2 = sorted(L,key=by_score)
print(L2)





