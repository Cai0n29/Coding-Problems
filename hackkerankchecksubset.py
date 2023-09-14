t = int(input())
for i in range(t):
    alen = int(input())
    a = input().split()
    blen = int(input())
    b = input().split()
    check = all(item in b for item in a)
    print(check)
