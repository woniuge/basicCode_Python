#没有使用generator（yield）


# 生成杨辉三角的一行
def createL(l):
    L = [1]
    for x in range(1,len(l)):
        L.append(l[x] + l[x-1])
    L.append(1)
    return L

# 打印
def printL(L,W):
    s = ""
    for x in L:
        s += str(x) + " "
    print(s.center(W))

L = [1]
row = int(input("输入行数："))
width = row * 4
for x in range(row):
    printL(L,width)
    L = createL(L)