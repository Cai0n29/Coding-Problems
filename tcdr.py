n = map(str, input().lower())
list = []
for alp in n:
    if alp != 'a' and alp != 'e' and alp != 'i' and alp != 'o' and alp !='u':
        list.append(alp)
print(str(list).replace(',','').replace('[','').replace(']','').replace("'",'').replace(" ", ''))