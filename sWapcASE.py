


k = input()
hello = []
for i in k:
    if i == i.upper():
        hello.append(i.lower())
    elif i == i.lower():
        hello.append(i.upper())

print(''.join(hello))

#def function
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

