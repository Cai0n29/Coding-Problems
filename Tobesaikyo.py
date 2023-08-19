n = int(input())
l = input().split()
p = [int(x) for x in l]
count = l.count(l[0])
if str(l[0]) == str(max(p)) and count == 1:
    print('0')
else:
    print(max(p) + 1 - p[0])


