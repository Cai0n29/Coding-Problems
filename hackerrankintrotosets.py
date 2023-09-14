n = int(input())
al =[]
for i in range(n):
    a, b, c, d = input().split()
    a = str(a)
    b = float(b)
    c = float(c)
    d = float(d)
    ap = (b+c+d)//3
    al.append(a, int(ap))
    print(ap)