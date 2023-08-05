N = int(input())
list = input().split()
list.sort()
emp = []
missing =0
intlist = [int(x) for x in list]
for i in range(1, N+1):
    emp.append(i)


missing = set(emp) - set(intlist)
print(str(missing).replace('{', '').replace('}', ''))
        