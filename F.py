s1 = input()
s2 = input()
a = []
b = []

for i in range(len(s1)):
    if s1[i] != "#":
        a.append(s1[i])
    else:
        if not a:
            continue
        else: 
            a.pop()

for i in range(len(s2)):
    if s2[i] != '#':
        b.append(s2[i])
    else:
        if not b:
            continue
        else: 
            b.pop()

if a == b:
    print("Yes")
else:
    print("No") 
