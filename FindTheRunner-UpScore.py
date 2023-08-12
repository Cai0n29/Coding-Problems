n = int(input())
lists = input().split()
inti = [int(x) for x in lists]
#Remove duplicates 
inti = list(set(inti))
inti.sort()
print(inti[-2])