s = input()
a = []
for i in s:
    if not a or i != a[-1]:
        a.append(i)
    else:
        a.pop()
if not a:
    print("YES")  
else:
    print("NO")   
