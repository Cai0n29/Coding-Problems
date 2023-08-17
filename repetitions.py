word = input().upper()
len = len(word)
maxi = 0
add = 0

for alp  in range(len-1):
    if word[alp] == word[alp + 1]:
        add += 1
        if maxi <= add:
            maxi = add
    elif word[alp] != word[alp+1]:
        add = 0
print(maxi+1)

   