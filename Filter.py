n = int(input())
l = input().split()
h = []
h= [int(x) for x in l]
even = []
for i in h:
    if i % 2 == 0:
        even.append(i)
print(str(even).replace(',', '').replace('[', '').replace(']',''))
        